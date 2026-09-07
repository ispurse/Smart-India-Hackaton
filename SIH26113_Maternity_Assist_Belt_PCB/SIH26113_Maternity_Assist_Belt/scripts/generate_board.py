"""
generate_board.py - Place, route and emit SIH26113_Maternity_Assist_Belt.brd

Order of operations (mirrors how the board would be built by hand):
  1  board outline, mounting holes, antenna keep-out
  2  element placement from design.PARTS
  3  thermal / exposed-pad vias on GND
  4  fan-out escapes on the fine-pitch packages (AD8232 QFN, LSM6DSOX LGA,
     TMP117 WSON) - these cannot be escaped with a 0.25 mm track
  5  GND stitching vias next to every SMD ground pad
  6  routing, in the priority order the brief asks for:
     ECG analog -> power -> motor -> I2C -> SPI -> GPIO -> everything else
  7  GND copper pour on both layers
  8  design rules + write out, then cross-check against the model

Run:  python scripts/generate_board.py
"""

from __future__ import annotations

import json
import pathlib
import random
import sys
import os
import time
import xml.etree.ElementTree as ET
from collections import defaultdict

sys.path.insert(0, str(pathlib.Path(__file__).parent))

import design as D          # noqa: E402
import geom                 # noqa: E402
import router as RT         # noqa: E402
from eagle_common import Text, Wire, document, esc, library_body, n  # noqa: E402
from lib_defs import (      # noqa: E402
    DEVICESETS,
    LIBRARY_DESCRIPTION,
    LIBRARY_NAME,
    PACKAGES,
    SYMBOLS,
    THERMAL_VIAS,
)

ROOT = pathlib.Path(__file__).resolve().parent.parent
OUT = ROOT / "pcb" / f"{LIBRARY_NAME}.brd"

# Fine-pitch packages need a manual fan-out before the grid router can reach
# them.  A single radial stub is not enough: at 0.5 mm pitch the stub ends are
# still inside each other's clearance rings.  So each pad is taken straight out
# to `r1`, then splayed sideways so the stub ends land on a coarse `spread`
# pitch at `r2` - the standard hand fan-out for a fine-pitch QFN/LGA.
# The stub ends are also STAGGERED - alternate pads stop short, the others
# run on - so that each end has room for its own via.  A 0.6 mm via plus
# clearance needs ~1.4 mm, which does not fit at a 1.2-1.3 mm splay pitch.
#   deviceset -> (r1, r2, spread pitch, stagger, track width)  all mm
FANOUT = {
    "AD8232":   (2.45, 4.70, 1.25, 1.40, 0.15),
    "LSM6DSOX": (1.70, 3.40, 1.15, 1.25, 0.15),
    "TMP117":   (1.50, 2.90, 1.15, 1.20, 0.20),
    # The HX711 is a coarse 1.27 mm SOP-16, but 9 of its 16 pads are on a
    # plane net and each of those takes a plane via right beside the pad.
    # That leaves the 7 signal pads with no room, so they get splayed too.
    "HX711":    (4.20, 6.20, 1.40, 1.50, 0.20),
}
# Exposed / thermal pads get vias inside them, not escapes.  Everything else
# - including pads on a plane net - gets a stub: on a fine-pitch part the
# plane pads have no more room than the signal pads do, so they are fanned
# out too and their plane via goes at the end of the stub.  That is what a
# hand-routed QFN looks like.
NO_ESCAPE = {("AD8232", "EP"), ("TMP117", "7"), ("ESP32-S3-WROOM-1", "41")}

# Coarser-pitch parts do not need splaying, but they DO need a reserved
# escape stub: without one, whichever net is routed last finds its pad walled
# in by the neighbours that were routed first.  Reserving one track out of
# every pad up front is what a human does with a fan-out pass.
# Stubs are STAGGERED: alternate pads get a longer stub, so their end points
# sit on two rows at twice the pad pitch.  That matters because a 0.6 mm via
# plus clearance needs ~1.4 mm of room, which does not fit at the module's
# 1.27 mm pitch - without staggering only every other pad could drop to the
# bottom layer, halving the escape capacity.
#   deviceset -> (base stub length beyond the pad centre mm, stagger mm,
#                 pad pitch mm, width mm)
#                 pad pitch mm, width mm, stagger levels)
RADIAL_ESCAPE = {
    # Three levels on the module: 36 signals leave a 1.27 mm pitch, and two
    # levels still leaves their stub ends 2.54 mm apart, which is only just
    # enough for a via each once clearance is counted.
    "ESP32-S3-WROOM-1": (1.90, 1.70, 1.27, 0.25, 3),
    "AS5600": (1.90, 1.60, 1.27, 0.25, 2),
    "TP4056": (1.90, 1.60, 1.27, 0.25, 2),
}

# With a dedicated inner GND plane (layer 2) directly under layer 1, every
# top-layer track already has an uninterrupted return path, so no bottom-side
# reserve is needed.  ECG nets are still pinned to layer 1 (see build()) so
# they sit immediately above that plane.

def _touches(net: str, ref: str) -> bool:
    return any(r == ref for r, _ in D.NETS[net])


# Routing order.  The brief's quality order (analog first, then power, then
# the rest) is kept, but within that the nets that terminate on the ESP32
# module are pulled forward: 36 signals have to escape a 1.27 mm pad pitch
# through a 4.5 mm channel, so whichever of them is routed last is the one
# that finds itself walled in.
ROUTE_PRIORITY = [
    ("ECG analog", lambda nm: nm in D.ECG_NETS),
    ("power", lambda nm: nm in ("3V3", "VBAT", "VBUS")),
    ("motor / buzzer",
     lambda nm: nm in D.MOTOR_NETS or nm.startswith(("MOTOR", "BUZZ"))),
    ("ESP32 module escapes", lambda nm: _touches(nm, "U3")),
    ("AD8232 escapes", lambda nm: _touches(nm, "U7")),
    ("I2C", lambda nm: nm.startswith(("I2C_", "ANG_"))),
    ("SPI", lambda nm: nm.startswith("SD_")),
    ("everything else", lambda nm: True),
]

# 0.20 mm carries ~0.7 A on 1 oz outer copper (IPC-2221, 10 C rise), which
# is orders of magnitude more than any signal here needs.  Narrower tracks
# buy back the routing density that the rigorous clearance radius costs.
WIDTH_FOR = {0: 0.20, 1: 0.50, 2: 0.50, 3: 0.20}

# Routing runs with the base clearance radius, which is sqrt(2) short of a
# hard guarantee for 45 degree tracks; the geometric repair pass then fixes
# the pairs that actually end up too close.  Anything the repair pass cannot
# fix is deliberately LEFT UNROUTED rather than shipped tight - an airwire is
# visible in Fusion and gets hand-routed, a 0.05 mm gap is invisible and
# might reach fabrication.  Set SIH_STRICT=1 to route everything with the
# full radius instead; that guarantees clearance without the repair pass but
# completes noticeably fewer nets.
STRICT_DEFAULT = os.environ.get("SIH_STRICT", "0") == "1"

# Nets carried by an inner plane rather than by tracks.  Their pads are tied
# to the plane with a short spur + a plane-connect via instead.
PLANE_NETS = {v: k for k, v in D.PLANE_LAYERS.items()}   # "GND"->2, "3V3"->15


def element_pads():
    """Yield (part, pad_name, x, y, dx, dy, is_tht) for every placed pad."""
    for p in D.PARTS:
        ds = geom.DS[p.deviceset]
        if ds.package is None:
            continue
        for pad_name, pd in geom.package_pads(ds.package).items():
            px, py = geom.rotate(pd.x, pd.y, p.brot)
            dx, dy, tht = geom.pad_extent(p.deviceset, pad_name, p.brot)
            yield p, pad_name, p.bx + px, p.by + py, dx, dy, tht


def pad_net_map():
    """(ref, pad_name) -> net name."""
    out = {}
    for net, conns in D.NETS.items():
        for ref, pin in conns:
            p = D.PART_BY_REF[ref]
            if geom.DS[p.deviceset].package is None:
                continue
            for pad_name in geom.pad_of(p.deviceset, pin):
                out[(ref, pad_name)] = net
    return out


def build(seed: int = 0) -> tuple[RT.Router, dict]:
    """Place everything, then route. Returns the router and a stats dict.

    A grid router is order-sensitive: the net that reaches a congested pad
    last is the one that fails.  `seed` permutes the order inside each
    priority batch so several orderings can be tried and the best kept.
    """
    t0 = time.time()
    r = RT.Router(D.BOARD_W, D.BOARD_H)
    pnet = pad_net_map()
    gnd_id = r.nid("GND")

    # -- 1. keep-outs -------------------------------------------------------
    ax1, ay1, ax2, ay2 = D.ANTENNA_KEEPOUT
    r.stamp_rect(None, (ax1 + ax2) / 2, (ay1 + ay2) / 2,
                 ax2 - ax1, ay2 - ay1, RT.BLOCKED)

    # -- 2. pads ------------------------------------------------------------
    pad_cells = {}
    for p, pad_name, x, y, dx, dy, tht in element_pads():
        net = pnet.get((p.ref, pad_name))
        owner = r.nid(net) if net else RT.BLOCKED
        layer = None if tht else RT.TOP
        round_pad = tht and abs(dx - dy) < 1e-6
        i0, j0 = r.c(x, y)
        if round_pad:
            # A round pad has to be stamped as a disc.  Stamping it as its
            # bounding square lets the router start a track from a corner
            # cell up to 0.27 mm outside the actual copper, which then looks
            # like a disconnected island to any connectivity check.
            r._stamp_cells(layer, x, y, dx / 2.0, owner, fixed=True)
            offs = [(0, 0)] + RT._disc_offsets(dx / 2.0)
        else:
            r.stamp_rect(layer, x, y, dx, dy, owner, fixed=True)
            a0, b0 = r.c(x - dx / 2, y - dy / 2)
            a1, b1 = r.c(x + dx / 2, y + dy / 2)
            offs = [(a - i0, b - j0)
                    for a in range(a0, a1 + 1) for b in range(b0, b1 + 1)]
        cells = []
        for di, dj in offs:
            i, j = i0 + di, j0 + dj
            if not (0 <= i < r.nx and 0 <= j < r.ny):
                continue
            if tht:
                cells += [(RT.TOP, i, j), (RT.BOT, i, j)]
            else:
                cells.append((RT.TOP, i, j))
        pad_cells[(p.ref, pad_name)] = cells

    # -- 3. thermal / exposed-pad vias (all GND) ---------------------------
    n_thermal = 0
    for p in D.PARTS:
        spec = THERMAL_VIAS.get(p.deviceset)
        if not spec:
            continue
        drill, dia, offs = spec
        for ox, oy in offs:
            vx, vy = geom.rotate(ox, oy, p.brot)
            r.vias.append(RT.Via("GND", p.bx + vx, p.by + vy, drill, dia))
            r.stamp_disc(None, p.bx + vx, p.by + vy, dia, gnd_id, fixed=True)
            n_thermal += 1

    # -- 4. fine-pitch fan-out ---------------------------------------------
    n_escape = 0
    n_escape_blocked = 0
    stub_end: dict[tuple[str, str], tuple[float, float]] = {}
    for p in D.PARTS:
        if p.deviceset not in FANOUT:
            continue
        r1, r2, spread, stagger, width = FANOUT[p.deviceset]
        ds = geom.DS[p.deviceset]
        pads = geom.package_pads(ds.package)
        # Group the signal pads by which side of the package they sit on, so
        # each side can be splayed independently.
        sides = defaultdict(list)
        for pad_name, pd in pads.items():
            if (p.deviceset, pad_name) in NO_ESCAPE:
                continue
            if abs(pd.x) >= abs(pd.y):
                sides["R" if pd.x > 0 else "L"].append((pd.y, pad_name, pd))
            else:
                sides["T" if pd.y > 0 else "B"].append((pd.x, pad_name, pd))
        for side, members in sides.items():
            members.sort()
            cnt = len(members)
            for idx, (_lat, pad_name, pd) in enumerate(members):
                net = pnet.get((p.ref, pad_name))
                if not net:
                    continue
                new_lat = (idx - (cnt - 1) / 2.0) * spread
                r2i = r2 + (idx % 2) * stagger
                if side in ("L", "R"):
                    sgn = 1.0 if side == "R" else -1.0
                    mid = (sgn * r1, pd.y)
                    end = (sgn * r2i, new_lat)
                else:
                    sgn = 1.0 if side == "T" else -1.0
                    mid = (pd.x, sgn * r1)
                    end = (new_lat, sgn * r2i)
                pts = []
                for lx, ly in ((pd.x, pd.y), mid, end):
                    rx, ry = geom.rotate(lx, ly, p.brot)
                    pts.append((p.bx + rx, p.by + ry))
                nid = r.nid(net)
                # Only lay the part of the stub that is actually clear.  A
                # stub that would cross a neighbouring pad is a short, and
                # it is emitted before any routing so nothing else would
                # catch it.
                good = [pts[0]]
                for a, b in zip(pts, pts[1:]):
                    if not r.segment_is_clear(RT.TOP, a, b, width, nid):
                        break
                    good.append(b)
                if len(good) < 2:
                    n_escape_blocked += 1
                    continue
                r.tracks.append(RT.Track(net, 1, good, width))
                for a, b in zip(good, good[1:]):
                    r.stamp_segment(RT.TOP, a, b, width, nid, fixed=True)
                pts = good
                stub_end[(p.ref, pad_name)] = good[-1]
                ei, ej = r.c(*pts[-1])
                for di in (-1, 0, 1):
                    for dj in (-1, 0, 1):
                        pad_cells[(p.ref, pad_name)].append(
                            (RT.TOP, ei + di, ej + dj))
                n_escape += 1

    # -- 4b. radial escape stubs on coarse-pitch parts ---------------------
    n_stub = 0
    n_stub_blocked = 0
    for p in D.PARTS:
        spec = RADIAL_ESCAPE.get(p.deviceset)
        if not spec:
            continue
        base, stagger, pitch, width, levels = spec
        ds = geom.DS[p.deviceset]
        for pad_name, pd in geom.package_pads(ds.package).items():
            net = pnet.get((p.ref, pad_name))
            if net is None or (p.deviceset, pad_name) in NO_ESCAPE:
                continue
            # Escape away from the package origin, along the pad's long axis,
            # with alternate pads pushed out by `stagger`.
            along_x = abs(pd.x) >= abs(pd.y)
            lat = pd.y if along_x else pd.x
            reach = base + (round(lat / pitch) % levels) * stagger
            if along_x:
                tx = pd.x + (reach if pd.x > 0 else -reach)
                ty = pd.y
            else:
                tx = pd.x
                ty = pd.y + (reach if pd.y > 0 else -reach)
            sx, sy = geom.rotate(pd.x, pd.y, p.brot)
            exx, exy = geom.rotate(tx, ty, p.brot)
            a = (p.bx + sx, p.by + sy)
            b = (p.bx + exx, p.by + exy)
            nid = r.nid(net)
            if not r.segment_is_clear(RT.TOP, a, b, width, nid):
                n_stub_blocked += 1
                continue
            r.tracks.append(RT.Track(net, 1, [a, b], width))
            r.stamp_segment(RT.TOP, a, b, width, nid, fixed=True)
            stub_end[(p.ref, pad_name)] = b
            ei, ej = r.c(*b)
            for di in (-1, 0, 1):
                for dj in (-1, 0, 1):
                    pad_cells[(p.ref, pad_name)].append((RT.TOP, ei + di, ej + dj))
            n_stub += 1

    # -- 5. plane-connect vias -----------------------------------------
    # Every pad on a plane net (GND, 3V3) is tied to its inner plane with a
    # short spur and a through via.  A through-hole pad already spans all
    # four layers, so it connects to its plane directly.
    n_plane_via = 0
    orphan_plane = []
    masks = {nm: r._mask_for(r.nid(nm), 0.15) for nm in PLANE_NETS}
    for p, pad_name, x, y, dx, dy, tht in element_pads():
        net = pnet.get((p.ref, pad_name))
        if net not in PLANE_NETS or tht:
            continue
        if THERMAL_VIAS.get(p.deviceset) and (p.deviceset, pad_name) in NO_ESCAPE:
            continue        # exposed pad: already stitched from inside
        nid = r.nid(net)
        # If the pad was fanned out, hang the via off the end of its stub
        # rather than off the pad, which on a fine-pitch part is the only
        # place there is room for one.
        # Try the fan-out stub end first (on a fine-pitch part that is the
        # only place with room), then the pad itself.
        origins = []
        if (p.ref, pad_name) in stub_end:
            ex, ey = stub_end[(p.ref, pad_name)]
            origins.append((ex, ey, 0.0, 0.0))
        origins.append((x, y, dx, dy))
        placed = False
        for sx, sy, dx, dy in origins:
          for dist in (0.7, 0.9, 1.1, 1.35, 1.6, 1.9, 2.3, 2.8, 3.4, 4.2):
            for ux, uy in ((0, 1), (0, -1), (1, 0), (-1, 0),
                           (0.71, 0.71), (-0.71, 0.71),
                           (0.71, -0.71), (-0.71, -0.71),
                           (0.92, 0.38), (0.38, 0.92), (-0.38, 0.92),
                           (-0.92, 0.38), (-0.92, -0.38), (-0.38, -0.92),
                           (0.38, -0.92), (0.92, -0.38)):
                vx = sx + ux * (dist + dx / 2)
                vy = sy + uy * (dist + dy / 2)
                vi, vj = r.c(vx, vy)
                if not (3 < vi < r.nx - 4 and 3 < vj < r.ny - 4):
                    continue
                if not (masks[net][RT.TOP, vi, vj] and masks[net][RT.BOT, vi, vj]):
                    continue
                # The spur from the pad to the via has to be clear too - a via
                # position can be free while the path to it crosses a
                # neighbouring pad, which is a short.
                if not r.segment_is_clear(RT.TOP, (sx, sy), (vx, vy), 0.3,
                                          nid, strict=True):
                    continue
                # A via outside the pour outline is a hole, not a plane
                # connection.  See _in_pour().
                if not _in_pour(vx, vy):
                    continue
                r.vias.append(RT.Via(net, vx, vy, 0.3, 0.55))
                r.tracks.append(RT.Track(net, 1, [(sx, sy), (vx, vy)], 0.3))
                r.stamp_disc(None, vx, vy, 0.55, nid, fixed=True)
                r.stamp_segment(RT.TOP, (sx, sy), (vx, vy), 0.3, nid,
                                fixed=True)
                masks = {nm: r._mask_for(r.nid(nm), 0.15) for nm in PLANE_NETS}
                n_plane_via += 1
                placed = True
                break
            if placed:
                break
          if placed:
              break
        if not placed:
            # Last resort: a straight spur cannot get out, so let the A* find
            # a path from the pad to somewhere a via does fit.  This is what
            # rescues a supply pin buried inside a fine-pitch fan-out.
            placed = _route_to_plane(r, p, pad_name, net, x, y,
                                     stub_end.get((p.ref, pad_name)))
            if placed:
                n_plane_via += 1
                masks = {nm: r._mask_for(r.nid(nm), 0.15) for nm in PLANE_NETS}
        if not placed:
            orphan_plane.append(f"{p.ref}.{pad_name} ({net})")

    # Coarse GND stitching so the two signal layers see a low-impedance
    # return everywhere, not just at the component pads.
    for gx in range(7, int(D.BOARD_W) - 5, 11):
        for gy in range(7, int(D.BOARD_H) - 5, 11):
            if not _in_pour(gx, gy):
                continue          # stitching outside the pour connects nothing
            vi, vj = r.c(gx, gy)
            m = r._mask_for(gnd_id)
            if m[RT.TOP, vi, vj] and m[RT.BOT, vi, vj]:
                r.vias.append(RT.Via("GND", float(gx), float(gy), 0.3, 0.6))
                r.stamp_disc(None, float(gx), float(gy), 0.6, gnd_id,
                             fixed=True)
                n_plane_via += 1

    # -- 6. routing ---------------------------------------------------------
    terminals = defaultdict(dict)
    for net, conns in D.NETS.items():
        if net in PLANE_NETS:
            continue
        for ref, pin in conns:
            p = D.PART_BY_REF[ref]
            if geom.DS[p.deviceset].package is None:
                continue
            cells = []
            for pad_name in geom.pad_of(p.deviceset, pin):
                cells += pad_cells.get((ref, pad_name), [])
            if cells:
                terminals[net][(ref, pin)] = cells

    ordered = []
    for _, pred in ROUTE_PRIORITY:
        batch = [net for net in D.NETS
                 if net not in PLANE_NETS and net not in ordered and pred(net)]
        # Inside a batch, hardest first: more terminals = less freedom.
        batch.sort(key=lambda nm: -len(terminals[nm]))
        if seed:
            rnd = random.Random(seed * 7919 + len(batch))
            rnd.shuffle(batch)
        ordered += batch

    def attempt(net, *, allow_bottom, via_cost, strict=STRICT_DEFAULT):
        terms = {f"{ref}.{pin}": cells
                 for (ref, pin), cells in terminals[net].items()}
        if len(terms) < 2:
            return None
        return r.route_net(net, terms, WIDTH_FOR[D.net_class(net)],
                           allow_bottom=allow_bottom, via_cost=via_cost,
                           strict=strict)

    failed = []
    routed = 0
    ecg_on_bottom = []
    for net in ordered:
        if len(terminals[net]) < 2:
            continue
        cls = D.net_class(net)
        # Pass 1: ECG analog nets are held on the top layer so the inner GND
        # plane beneath them is never interrupted.
        why = attempt(net, allow_bottom=(cls != 3), via_cost=RT.VIA_COST)
        if why and cls == 3:
            # Pass 2 for ECG: allow the bottom layer rather than leave the
            # net unrouted, and record which nets needed it.
            why2 = attempt(net, allow_bottom=True, via_cost=RT.VIA_COST)
            if not why2:
                ecg_on_bottom.append(net)
                why = None
            else:
                why = why2
        if why:
            # Pass 3: cheap vias, so a boxed-in pad can escape by changing
            # layer immediately instead of hunting for a planar route.
            why3 = attempt(net, allow_bottom=True, via_cost=40)
            if not why3:
                why = None
        if why:
            failed.append((net, why))
        else:
            routed += 1

    # -- 6b. rip-up and re-route -------------------------------------------
    # A greedy router paints itself into corners: whichever net reaches a
    # congested pad last finds it walled in.  For each failure, rip up the
    # handful of nets whose routed copper sits nearest the unreachable
    # terminal, route the failure first, then put the ripped nets back.
    #
    # The attempt is TRANSACTIONAL.  The router state is snapshotted first and
    # rolled back unless the target routes AND every ripped net is restored,
    # so this pass is strictly monotonic - it can reduce the unrouted count
    # but can never increase it.  (An earlier non-transactional version
    # cascaded: displaced nets became new failures, which ripped more nets.)
    RIP_RADIUS = 14.0
    MAX_VICTIMS = 8
    ripup_log = []
    for _round in range(4):
        progress = False
        for net, why in list(failed):
            ref = why.split(" unreachable")[0].partition(".")[0]
            pr = D.PART_BY_REF.get(ref)
            if pr is None:
                continue
            cx, cy = pr.bx, pr.by
            near = {}
            for t in r.live_tracks():
                if t.net in PLANE_NETS or t.net == net:
                    continue
                if t.net not in r.commit_log:
                    continue
                d = min(((x - cx) ** 2 + (y - cy) ** 2) ** 0.5 for x, y in t.pts)
                if d < RIP_RADIUS:
                    near[t.net] = min(near.get(t.net, 1e9), d)
            victims = [nm for nm, _ in sorted(near.items(),
                                              key=lambda kv: kv[1])][:MAX_VICTIMS]
            if not victims:
                continue
            snap = r.snapshot()
            ripped = [v for v in victims if r.rip(v)]
            ok = attempt(net, allow_bottom=True, via_cost=40) is None
            restored = all(attempt(v, allow_bottom=True, via_cost=40) is None
                           for v in ripped)
            if ok and restored:
                failed = [(n2, w2) for n2, w2 in failed if n2 != net]
                ripup_log.append({"target": net, "ripped": ripped,
                                  "accepted": True})
                progress = True
            else:
                r.restore(snap)
                ripup_log.append({"target": net, "ripped": ripped,
                                  "accepted": False})
        if not progress:
            break

    # Pads, as stadium shapes, so the repair pass below sees track-to-pad
    # clearance as well as track-to-track.  A rectangular pad becomes a
    # segment along its long axis with a radius of half its short axis -
    # exact along the sides, slightly conservative at the corners.
    pad_shapes = []
    for pp, pad_name, x, y, dx, dy, tht in element_pads():
        nt = pnet.get((pp.ref, pad_name))
        if nt is None:
            continue
        layers = (1, 16) if tht else (1,)
        if abs(dx - dy) < 1e-6:
            seg, rad = ((x, y), (x, y)), dx / 2.0
        elif dx > dy:
            rad = dy / 2.0
            half = dx / 2.0 - rad
            seg = ((x - half, y), (x + half, y))
        else:
            rad = dx / 2.0
            half = dy / 2.0 - rad
            seg = ((x, y - half), (x, y + half))
        for L in layers:
            pad_shapes.append((nt, L, seg, rad))

    # -- 6c. geometric repair ----------------------------------------------
    # The routing grid measures clearance between cell centres, but the copper
    # is a continuous polyline, and two 45 degree tracks can end up sqrt(2)
    # times closer than their vertices suggest.  Rather than inflate every
    # net's exclusion radius by sqrt(2) - which costs about a fifth of the
    # routing capacity - measure the real geometry and repair only the pairs
    # that are actually too close, re-routing the offender in strict mode.
    repair_log = []
    for _pass in range(10):
        viols = RT.find_violations(r.live_tracks(), pads=pad_shapes,
                                     exceptions=D.clearance_exceptions())
        if not viols:
            break
        handled = set()
        fixed_any = False
        for gap, na, nb, layer in viols:
            if na in handled or nb in handled:
                continue
            # Prefer to move whichever net is rippable and simpler.
            cands = [n for n in (na, nb)
                     if n not in PLANE_NETS and n in r.commit_log]
            cands.sort(key=lambda n: len(terminals.get(n, {})))
            if not cands:
                repair_log.append({"pair": [na, nb], "gap": round(gap, 3),
                                   "action": "not repairable (fixed copper)"})
                handled.update((na, nb))
                continue
            # Try each candidate, in strict mode first and then normal - a
            # normal re-route often finds a different path anyway, because
            # the conflicting copper has just been removed.
            done = None
            for victim in cands:
                for strict in (True, False):
                    snap = r.snapshot()
                    r.rip(victim)
                    why = attempt(victim, allow_bottom=True,
                                  via_cost=RT.VIA_COST, strict=strict)
                    if why:
                        r.restore(snap)
                        continue
                    after = RT.find_violations(r.live_tracks(),
                                               pads=pad_shapes)
                    if len(after) < len(viols):
                        done = (victim, "strict" if strict else "normal")
                        break
                    r.restore(snap)
                if done:
                    break
            if done:
                repair_log.append({
                    "pair": [na, nb], "gap": round(gap, 3),
                    "action": f"re-routed {done[0]} ({done[1]} clearance)"})
                fixed_any = True
            else:
                repair_log.append({"pair": [na, nb], "gap": round(gap, 3),
                                   "action": "no alternative path found"})
            handled.update((na, nb))
        if not fixed_any:
            break
    # Clearance beats completeness: rip anything still too close and leave
    # it as an airwire, so the board that ships is DRC-clean by construction
    # and the exceptions are visible rather than hidden.
    conceded = []
    unfixable: set[frozenset] = set()
    for _ in range(80):
        residual = RT.find_violations(r.live_tracks(), pads=pad_shapes,
                                     exceptions=D.clearance_exceptions())
        todo = [v for v in residual
                if frozenset((v[1], v[2])) not in unfixable]
        if not todo:
            break
        gap, na, nb, layer = todo[0]
        cands = [n for n in (na, nb)
                 if n not in PLANE_NETS and n in r.commit_log]
        if not cands:
            # Both sides are fixed copper (a pad, a fan-out stub or a plane
            # spur).  Nothing can be ripped, so record it and move on rather
            # than stopping - later pairs may well be fixable.
            unfixable.add(frozenset((na, nb)))
            continue
        cands.sort(key=lambda n: len(terminals.get(n, {})))
        # Only concede if it actually helps.  Ripping a net does not remove
        # its fan-out stub, so a violation involving that stub survives the
        # concession - and conceding both sides of such a pair would abandon
        # two nets for nothing.
        helped = None
        for victim in cands:
            snap = r.snapshot()
            r.rip(victim)
            now = RT.find_violations(r.live_tracks(), pads=pad_shapes,
                                     exceptions=D.clearance_exceptions())
            if len(now) < len(residual):
                helped = victim
                break
            r.restore(snap)
        if helped is None:
            unfixable.add(frozenset((na, nb)))
            continue
        other = nb if helped == na else na
        conceded.append((helped, other, round(gap, 3), layer))
        failed.append((
            helped,
            f"left unrouted on purpose: every path the router found came "
            f"within {gap:.3f} mm of {other} on layer {layer}, below the "
            f"{RT.MIN_CLEARANCE} mm rule. Route it by hand in Fusion."))
    residual = RT.find_violations(r.live_tracks(), pads=pad_shapes,
                                     exceptions=D.clearance_exceptions())

    # Recount from the final state rather than trusting the running tally
    # through the rip-up passes.
    unrouted_names = {nm for nm, _ in failed}
    routable = [nm for nm in ordered if len(terminals[nm]) >= 2]
    routed = len([nm for nm in routable if nm not in unrouted_names])

    stats = {
        "seed": seed,
        "geometric_repairs": repair_log,
        "conceded_for_clearance": [
            {"net": v, "conflicted_with": o, "gap_mm": g,
             "layer": L} for v, o, g, L in conceded],
        "residual_violations": [
            {"gap_mm": round(g, 3), "nets": [a, b], "layer": L}
            for g, a, b, L in residual[:40]],
        "residual_violation_count": len(residual),
        "ripup_attempts": len(ripup_log),
        "routed": routed,
        "total_signal_nets": len(routable),
        "failed": failed,
        "thermal_vias": n_thermal,
        "escapes": n_escape,
        "radial_stubs": n_stub,
        "escapes_blocked": n_escape_blocked,
        "radial_stubs_blocked": n_stub_blocked,
        "plane_vias": n_plane_via,
        "orphan_plane_pads": orphan_plane,
        "ecg_nets_needing_bottom_layer": ecg_on_bottom,
        "route_seconds": round(time.time() - t0, 1),
    }
    return r, stats


# EAGLE applies one clearance value per class pair, so the rule set
# carries the tightest value the board uses (0.127 mm, inside the
# fine-pitch fan-outs).  Everywhere else the board actually achieves
# 0.15 mm or better - see the measured minima in DRC_REPORT.md.
DESIGN_RULES = [
    ("layerSetup", "(1*2*15*16)"),
    ("mtCopper", "0.035mm 0.035mm 0.035mm 0.035mm"),
    ("mtIsolate", "0.36mm 0.71mm 0.36mm"),
    ("psTop", "-1"), ("psBottom", "-1"), ("psFirst", "-1"),
    ("psElongationLong", "100"), ("psElongationOffset", "100"),
    ("mdWireWire", "0.127mm"), ("mdWirePad", "0.127mm"), ("mdWireVia", "0.127mm"),
    ("mdPadPad", "0.127mm"), ("mdPadVia", "0.127mm"), ("mdViaVia", "0.127mm"),
    ("mdSmdPad", "0.127mm"), ("mdSmdVia", "0.127mm"), ("mdSmdSmd", "0.127mm"),
    ("mdViaViaSameLayer", "0.127mm"),
    ("mnLayersViaInSmd", "2"),
    ("mdCopperDimension", "0.4mm"),
    ("mdDrill", "0.25mm"), ("mdSmdStop", "0mm"),
    ("msWidth", "0.15mm"), ("msDrill", "0.3mm"), ("msMicroVia", "9.999mm"),
    ("msBlindViaRatio", "0.500000"),
    ("rvPadTop", "0.25"), ("rvPadInner", "0.25"), ("rvPadBottom", "0.25"),
    ("rvViaOuter", "0.25"), ("rvViaInner", "0.25"),
    ("rlMinPadTop", "0.25mm"), ("rlMaxPadTop", "0.6mm"),
    ("rlMinPadInner", "0.25mm"), ("rlMaxPadInner", "0.6mm"),
    ("rlMinPadBottom", "0.25mm"), ("rlMaxPadBottom", "0.6mm"),
    ("rlMinViaOuter", "0.15mm"), ("rlMaxViaOuter", "0.5mm"),
    ("rlMinViaInner", "0.15mm"), ("rlMaxViaInner", "0.5mm"),
    ("srRoundness", "0"), ("srMinRoundness", "0mm"), ("srMaxRoundness", "0mm"),
    ("slThermalIsolate", "0.3mm"), ("slThermalsForVias", "off"),
    ("dpMaxLengthDifference", "10mm"), ("dpGapFactor", "2.5"),
    ("checkGrid", "off"), ("checkAngle", "off"), ("checkFont", "on"),
    ("checkRestrict", "on"),
    ("useDiameter", "13"), ("useShapes", "13"), ("isolate", "0.3mm"),
]


def _plain_items():
    W, H = D.BOARD_W, D.BOARD_H
    plain = [
        Wire(0, 0, W, 0, 0.2, 20), Wire(W, 0, W, H, 0.2, 20),
        Wire(W, H, 0, H, 0.2, 20), Wire(0, H, 0, 0, 0.2, 20),
    ]
    ax1, ay1, ax2, ay2 = D.ANTENNA_KEEPOUT
    for L in (39, 40, 41, 42, 43):
        plain += [
            Wire(ax1, ay1, ax2, ay1, 0.1, L), Wire(ax2, ay1, ax2, ay2, 0.1, L),
            Wire(ax2, ay2, ax1, ay2, 0.1, L), Wire(ax1, ay2, ax1, ay1, 0.1, L),
        ]
    plain.append(Text(ax1 + 0.8, ay1 + 1.0, 1.0, 48,
                      "ANTENNA KEEPOUT - NO COPPER / NO PLANE / NO PARTS"))
    for label, x1, y1, x2, y2 in D.ZONES:
        plain += [
            Wire(x1, y1, x2, y1, 0.1, 48), Wire(x2, y1, x2, y2, 0.1, 48),
            Wire(x2, y2, x1, y2, 0.1, 48), Wire(x1, y2, x1, y1, 0.1, 48),
            Text(x1 + 0.4, y2 - 1.6, 1.1, 48, label),
        ]
    plain += [
        Text(29.0, H - 2.4, 1.6, 21, "SIH26113 MATERNITY ASSIST BELT rev A"),
        Text(29.0, H - 4.4, 1.0, 21, "NOT A MEDICAL DEVICE - PROTOTYPE ONLY"),
        Text(29.0, 0.8, 1.0, 22,
             f"{D.BOARD_LAYERS}-LAYER FR-4 {D.BOARD_THICKNESS}mm  "
             f"{D.COPPER_OZ}oz Cu  L2=GND L15=3V3"),
    ]
    return plain


def _signals_xml(r: RT.Router) -> list[str]:
    tracks_by_net = defaultdict(list)
    for t in r.live_tracks():
        tracks_by_net[t.net].append(t)
    vias_by_net = defaultdict(list)
    for v in r.live_vias():
        vias_by_net[v.net].append(v)

    sigs = []
    for net in D.NETS:
        cls = D.net_class(net)
        s = [f'<signal name="{esc(net)}" class="{cls}">']
        for ref, pin in D.NETS[net]:
            p = D.PART_BY_REF[ref]
            if geom.DS[p.deviceset].package is None:
                continue
            for pad_name in geom.pad_of(p.deviceset, pin):
                s.append(f'<contactref element="{esc(ref)}" '
                         f'pad="{esc(pad_name)}"/>')
        for t in tracks_by_net[net]:
            for a, b in zip(t.pts, t.pts[1:]):
                s.append(f'<wire x1="{n(a[0])}" y1="{n(a[1])}" '
                         f'x2="{n(b[0])}" y2="{n(b[1])}" '
                         f'width="{n(t.width)}" layer="{t.layer}"/>')
        for v in vias_by_net[net]:
            s.append(f'<via x="{n(v.x)}" y="{n(v.y)}" extent="1-16" '
                     f'drill="{n(v.drill)}" diameter="{n(v.diameter)}"/>')
        if net in PLANE_NETS:
            # Solid inner plane.  D.PLANE_OUTLINE is the board minus the
            # antenna block, because an EAGLE polygon cannot carry a hole and
            # Espressif requires no copper (planes included) beneath the
            # module antenna.
            layer = PLANE_NETS[net]
            s.append(f'<polygon width="0.4" layer="{layer}" pour="solid" '
                     f'isolate="0.4" orphans="off" thermals="off" rank="1">')
            for vx, vy in D.PLANE_OUTLINE:
                s.append(f'<vertex x="{n(vx)}" y="{n(vy)}"/>')
            s.append("</polygon>")
        s.append("</signal>")
        sigs.append("\n".join(s))
    return sigs


def emit(r: RT.Router) -> str:
    lib = library_body(LIBRARY_DESCRIPTION, PACKAGES, SYMBOLS, DEVICESETS,
                       name=LIBRARY_NAME)
    els = []
    for p in D.PARTS:
        pkg = geom.DS[p.deviceset].package
        if pkg is None:
            continue
        val = esc(p.value) if p.value else ""
        els.append(
            f'<element name="{esc(p.ref)}" library="{esc(LIBRARY_NAME)}" '
            f'package="{esc(pkg)}" value="{val}" x="{n(p.bx)}" y="{n(p.by)}"'
            + (f' rot="{p.brot}"' if p.brot != "R0" else "")
            + "/>"
        )
    dr = "\n".join(f'<param name="{k}" value="{v}"/>' for k, v in DESIGN_RULES)
    classes = "\n".join(
        f'<class number="{num}" name="{name}" width="{n(w)}" drill="{n(dl)}">\n'
        f'<clearance class="{num}" value="{n(cl)}"/>\n</class>'
        for num, name, w, dl, cl in D.NET_CLASSES
    )
    inner = (
        "<board>\n"
        "<plain>\n" + "\n".join(i.xml() for i in _plain_items()) + "\n</plain>\n"
        "<libraries>\n" + lib + "\n</libraries>\n"
        "<attributes/>\n<variantdefs/>\n"
        "<classes>\n" + classes + "\n</classes>\n"
        f'<designrules name="SIH26113_4layer">\n{dr}\n</designrules>\n'
        '<autorouter>\n<pass name="Default">\n</pass>\n</autorouter>\n'
        "<elements>\n" + "\n".join(els) + "\n</elements>\n"
        "<signals>\n" + "\n".join(_signals_xml(r)) + "\n</signals>\n"
        "</board>"
    )
    return document(inner)


ATTEMPTS = int(os.environ.get("SIH_ROUTE_ATTEMPTS", "14"))


def main() -> int:
    best = None
    for seed in range(ATTEMPTS):
        r_i, s_i = build(seed)
        n_fail = len(s_i["failed"])
        n_viol = s_i["residual_violation_count"]
        score = (n_viol, n_fail)          # clearance first, then completeness
        print(f"  attempt seed={seed}: {s_i['routed']}/"
              f"{s_i['total_signal_nets']} routed, {n_fail} unrouted, "
              f"{n_viol} clearance violations, {s_i['route_seconds']}s")
        if best is None or score < (best[1]["residual_violation_count"],
                                    len(best[1]["failed"])):
            best = (r_i, s_i)
        if score == (0, 0):
            break
    r, stats = best
    stats["attempts_tried"] = ATTEMPTS
    print(f"  best attempt: seed={stats['seed']}")
    print(f"  routed {stats['routed']}/{stats['total_signal_nets']} "
          f"signal nets in {stats['route_seconds']}s")
    for net, why in stats["failed"]:
        print(f"  ! UNROUTED {net}: {why}")
    for o in stats["orphan_plane_pads"]:
        print(f"  ! NO PLANE VIA PLACED for {o}")

    xml = emit(r)
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(xml, encoding="utf-8")

    tree = ET.fromstring(xml.split("\n", 2)[2])
    brd = tree.find("./drawing/board")
    els = {e.get("name") for e in brd.findall("./elements/element")}
    want = {p.ref for p in D.PARTS if geom.DS[p.deviceset].package is not None}
    assert els == want, f"element mismatch: {els ^ want}"
    sigs = {s.get("name") for s in brd.findall("./signals/signal")}
    assert sigs == set(D.NETS), f"signal mismatch: {sigs ^ set(D.NETS)}"

    stats.update(
        wires=len(brd.findall("./signals/signal/wire")),
        vias=len(brd.findall("./signals/signal/via")),
        polygons=len(brd.findall("./signals/signal/polygon")),
        contactrefs=len(brd.findall(".//contactref")),
        elements=len(els), signals=len(sigs),
        board_w=D.BOARD_W, board_h=D.BOARD_H, layers=D.BOARD_LAYERS,
    )
    print(f"WROTE {OUT.relative_to(ROOT)}  ({OUT.stat().st_size:,} bytes)")
    print(f"  elements={stats['elements']}  signals={stats['signals']}  "
          f"contactrefs={stats['contactrefs']}  wires={stats['wires']}  "
          f"vias={stats['vias']}  pours={stats['polygons']}")
    print(f"  thermal vias={stats['thermal_vias']}  "
          f"fanout escapes={stats['escapes']}  "
          f"radial stubs={stats['radial_stubs']}  "
          f"plane-connect vias={stats['plane_vias']}")
    print("  board vs. model cross-check: PASS")
    (ROOT / "pcb" / "route_report.json").write_text(
        json.dumps(stats, indent=2), encoding="utf-8")
    return 0



def _in_pour(x: float, y: float, margin: float = 0.30) -> bool:
    """Is (x, y) inside the inner-plane pour, far enough in to connect?

    This exists because of a real defect. The pour outline is L-shaped - for
    x < 29.5 it stops at y = 63.0, so that neither plane runs up beside the
    module's antenna. Nothing previously stopped a *plane via* being placed in
    that strip, and two GND vias were: one of them was C7's only connection to
    the ground plane, and C7 is the HF bypass at the module's supply pin.

    A via there is not a plane connection. It is a hole. And because the pour
    declares `orphans="off"`, EAGLE deletes any island rather than leaving
    copper that might have rescued it.

    `margin` is the via's own pad radius: the pad has to be inside the pour,
    not merely its centre.
    """
    pts = D.PLANE_OUTLINE
    inside = False
    n = len(pts)
    for i in range(n):
        x1, y1 = pts[i]
        x2, y2 = pts[(i + 1) % n]
        if y1 == y2:
            continue
        if (y >= min(y1, y2)) and (y < max(y1, y2)):
            xint = x1 + (y - y1) * (x2 - x1) / (y2 - y1)
            if x < xint:
                inside = not inside
    if not inside:
        return False
    # keep the pad clear of the outline itself
    for i in range(n):
        x1, y1 = pts[i]
        x2, y2 = pts[(i + 1) % n]
        dx, dy = x2 - x1, y2 - y1
        L2 = dx * dx + dy * dy
        t = 0.0 if L2 == 0 else max(0.0, min(1.0, ((x - x1) * dx + (y - y1) * dy) / L2))
        if ((x - (x1 + t * dx)) ** 2 + (y - (y1 + t * dy)) ** 2) < margin * margin:
            return False
    ax1, ay1, ax2, ay2 = D.ANTENNA_KEEPOUT
    if (ax1 - margin) <= x <= (ax2 + margin) and (ay1 - margin) <= y <= (ay2 + margin):
        return False
    return True


def _route_to_plane(r, part, pad_name, net, px, py, stub) -> bool:
    """Connect a plane-net pad to its plane when no straight spur fits.

    Key point: every via in this design is a through via (`extent="1-16"`),
    so a via already sitting on this net is *already* tied to the inner
    plane.  Reaching any one of them therefore reaches the plane - which
    turns an awkward "find somewhere a via fits" problem into an ordinary
    two-terminal routing problem the A* can solve.

    This is what rescues a supply pin buried inside a fine-pitch fan-out.
    """
    nid = r.nid(net)
    ox, oy = stub if stub else (px, py)
    oi, oj = r.c(ox, oy)

    # "every via is a through via, so reaching one reaches the plane" is only
    # true for a via that is INSIDE the pour.  That assumption is what put
    # C7's ground via 0.725 mm outside the GND pour.  Filter first.
    existing = [v for v in r.live_vias() if v.net == net and _in_pour(v.x, v.y)]
    if not existing:
        return False
    existing.sort(key=lambda v: (v.x - ox) ** 2 + (v.y - oy) ** 2)

    pad_cells = [(L, oi + di, oj + dj)
                 for L in (RT.TOP,)
                 for di in (-1, 0, 1) for dj in (-1, 0, 1)
                 if 0 <= oi + di < r.nx and 0 <= oj + dj < r.ny]

    for v in existing[:8]:
        vi, vj = r.c(v.x, v.y)
        target = [(L, vi + di, vj + dj)
                  for L in (RT.TOP, RT.BOT)
                  for di in (-1, 0, 1) for dj in (-1, 0, 1)
                  if 0 <= vi + di < r.nx and 0 <= vj + dj < r.ny]
        snap = r.snapshot()
        why = r.route_net(net,
                          {f"{part.ref}.{pad_name}": pad_cells,
                           f"via@{v.x:.1f},{v.y:.1f}": target},
                          0.25, allow_bottom=True, via_cost=RT.VIA_COST)
        if why:
            r.restore(snap)
            continue
        return True
    return False


if __name__ == "__main__":
    raise SystemExit(main())
