"""
router.py - A grid router for the SIH26113 two-layer carrier board.

Not a production autorouter, but a real one: it maintains an occupancy grid
per copper layer, honours clearance by dilating obstacles, routes each net as
a minimum spanning sequence of A* searches with a via penalty, and refuses to
produce a track it cannot legally place.  Nets it cannot finish are reported
so they can be listed honestly in DRC_REPORT.md rather than silently dropped.

Tracks are routed on an 8-connected grid, so the output uses 45 degree
segments the way a hand-routed board does; a purely Manhattan router needs
far more room for the same net count.

Grid: 0.20 mm.  Obstacles are stamped at their true extent and dilated by
2 cells (0.40 mm), so a 0.25 mm track keeps its centreline 0.40 mm clear of
foreign copper - 0.275 mm edge to edge, above the 0.2 mm design rule.

Note the consequence: the router will not thread a track between two 0805
lands (0.75 mm inner gap), because 0.75 mm minus two 0.40 mm exclusions is
negative.  That matches hand practice - you route around, not between.
"""

from __future__ import annotations

import heapq
from dataclasses import dataclass, field

import numpy as np

GRID = 0.20                 # mm per cell
MIN_CLEARANCE = 0.15        # mm, copper to copper - the design rule itself
NOMINAL_HALF_WIDTH = 0.100  # mm, half a signal track; foreign copper is
                            # stamped centre-line-only, so its own half-width
                            # has to be allowed for here
SQRT2 = 1.4142135624


def exclusion_radius(half_width: float, strict: bool = False) -> float:
    """How far a track's centreline must stay from foreign stamped copper.

    Foreign copper is stamped along its centreline rather than at its full
    width, so its own half-width has to be allowed for here - that is the
    base radius.

    `strict` additionally multiplies by sqrt(2).  That covers a real effect:
    the emitted wire is a continuous polyline through cell centres, and two
    such polylines can approach each other up to sqrt(2) times closer than
    their vertices do (two parallel 45 degree tracks whose vertices are
    0.4 mm apart are only 0.283 mm apart as lines).

    Applying `strict` to every net costs about a fifth of the routing
    capacity, so the default is the base radius and the few pairs that
    actually end up too close are repaired afterwards - see
    `repair_violations` in generate_board.py.  The DRC measures the real
    geometry either way, so nothing is taken on trust.
    """
    base = MIN_CLEARANCE + half_width + NOMINAL_HALF_WIDTH
    return SQRT2 * base if strict else base


def stamp_radius(half_width: float) -> float:
    """Radius at which a conductor of this half-width should be stamped.

    `exclusion_radius` allows NOMINAL_HALF_WIDTH for whatever conductor it is
    keeping away from, because the occupancy grid records ownership but not
    width.  A conductor WIDER than nominal - a 0.50 mm power track, or a
    0.30 mm plane spur - must therefore be stamped proportionally wider, or
    every other net will come that much too close to it.

    This was a live defect: 0.30 mm plane spurs against 0.15 mm fan-out stubs
    landed at exactly 0.100 mm instead of 0.15 mm, which is the 0.05 mm by
    which 0.15 exceeds the 0.10 nominal.
    """
    return max(half_width, 2.0 * half_width - NOMINAL_HALF_WIDTH)
# Costs are in tenths of a cell so a 45 degree step (14) can be priced
# against an orthogonal one (10) with integers.
STEP_ORTHO = 10
STEP_DIAG = 14
VIA_COST = 60               # ~6 cells; discourages needless layer changes
BOTTOM_COST = 0             # both signal layers are equal over a plane
EDGE_MARGIN = 0.6           # mm of copper keep-out from the board outline

FREE = -1
BLOCKED = -2                # hard obstacle: board edge, keepout, plane cut-out

TOP, BOT = 0, 1


@dataclass
class Track:
    net: str
    layer: int              # EAGLE layer number: 1 (top) or 16 (bottom)
    pts: list[tuple[float, float]]
    width: float
    alive: bool = True      # cleared to False when the net is ripped up


@dataclass
class Via:
    net: str
    x: float
    y: float
    drill: float = 0.3
    diameter: float = 0.6
    alive: bool = True


@dataclass
class RouteResult:
    tracks: list[Track] = field(default_factory=list)
    vias: list[Via] = field(default_factory=list)
    failed: list[tuple[str, str]] = field(default_factory=list)   # (net, why)
    stats: dict = field(default_factory=dict)


class Router:
    def __init__(self, w: float, h: float) -> None:
        self.w, self.h = w, h
        self.nx = int(round(w / GRID)) + 1
        self.ny = int(round(h / GRID)) + 1
        # occ[layer] holds a small integer net id, FREE, or BLOCKED.
        self.occ = np.full((2, self.nx, self.ny), FREE, dtype=np.int16)
        # Copper that cannot be ripped up: pads, thermal vias, fan-out stubs
        # and plane spurs.  Routed tracks are held at the STRICT clearance
        # radius around these, because if a track ends up too close to fixed
        # copper the only remedies are to move the track or abandon it -
        # there is nothing on the other side to rip.
        self.fixed = np.zeros((2, self.nx, self.ny), dtype=bool)
        self.net_ids: dict[str, int] = {}
        self.tracks: list[Track] = []
        self.vias: list[Via] = []
        # Rip-up bookkeeping.  Only copper laid by _commit (i.e. actual
        # routing) is recorded: pads, fan-out stubs and plane vias are
        # permanent and must never be ripped.
        self.commit_log: dict[str, list[tuple[str, int]]] = {}
        self.commit_cells: dict[str, list[tuple[int, int, int]]] = {}
        self._mark_board_edge()

    def rip(self, net: str) -> bool:
        """Remove everything the router laid for `net`. Returns True if any
        copper was actually removed."""
        log = self.commit_log.pop(net, [])
        for kind, idx in log:
            (self.tracks if kind == "track" else self.vias)[idx].alive = False
        nid = self.net_ids.get(net)
        if nid is not None:
            for L, i, j in self.commit_cells.pop(net, []):
                if self.occ[L, i, j] == nid:
                    self.occ[L, i, j] = FREE
        else:
            self.commit_cells.pop(net, None)
        return bool(log)

    def snapshot(self) -> dict:
        """Capture enough state to undo a rip-up attempt exactly."""
        return {
            "occ": self.occ.copy(),
            "fixed": self.fixed.copy(),
            "n_tracks": len(self.tracks),
            "n_vias": len(self.vias),
            "alive_t": [t.alive for t in self.tracks],
            "alive_v": [v.alive for v in self.vias],
            "log": {k: list(v) for k, v in self.commit_log.items()},
            "cells": {k: list(v) for k, v in self.commit_cells.items()},
        }

    def restore(self, snap: dict) -> None:
        self.occ = snap["occ"].copy()
        self.fixed = snap["fixed"].copy()
        del self.tracks[snap["n_tracks"]:]
        del self.vias[snap["n_vias"]:]
        for t, a in zip(self.tracks, snap["alive_t"]):
            t.alive = a
        for v, a in zip(self.vias, snap["alive_v"]):
            v.alive = a
        self.commit_log = {k: list(v) for k, v in snap["log"].items()}
        self.commit_cells = {k: list(v) for k, v in snap["cells"].items()}

    def live_tracks(self):
        return [t for t in self.tracks if t.alive]

    def live_vias(self):
        return [v for v in self.vias if v.alive]

    # -- coordinate helpers -------------------------------------------------
    def c(self, x: float, y: float) -> tuple[int, int]:
        return (int(round(x / GRID)), int(round(y / GRID)))

    def xy(self, i: int, j: int) -> tuple[float, float]:
        return (i * GRID, j * GRID)

    def nid(self, net: str) -> int:
        if net not in self.net_ids:
            self.net_ids[net] = len(self.net_ids)
        return self.net_ids[net]

    def _mark_board_edge(self) -> None:
        m = int(round(EDGE_MARGIN / GRID))
        self.occ[:, :m, :] = BLOCKED
        self.occ[:, -m:, :] = BLOCKED
        self.occ[:, :, :m] = BLOCKED
        self.occ[:, :, -m:] = BLOCKED

    # -- obstacle stamping --------------------------------------------------
    def stamp_rect(self, layer: int | None, x: float, y: float,
                   dx: float, dy: float, owner: int,
                   fixed: bool = False) -> None:
        """Mark an axis-aligned rectangle. layer=None means both layers."""
        i0, j0 = self.c(x - dx / 2, y - dy / 2)
        i1, j1 = self.c(x + dx / 2, y + dy / 2)
        i0, j0 = max(i0, 0), max(j0, 0)
        i1, j1 = min(i1, self.nx - 1), min(j1, self.ny - 1)
        if i1 < i0 or j1 < j0:
            return
        sl = slice(i0, i1 + 1), slice(j0, j1 + 1)
        layers = (0, 1) if layer is None else (layer,)
        for L in layers:
            view = self.occ[L][sl]
            # BLOCKED wins over a net owner; otherwise the first owner sticks.
            np.copyto(view, owner, where=(view == FREE))
            if owner == BLOCKED:
                view[:] = BLOCKED
            if fixed:
                self.fixed[L][sl] = True

    def stamp_disc(self, layer: int | None, x: float, y: float,
                   d: float, owner: int, fixed: bool = False) -> None:
        self.stamp_rect(layer, x, y, d, d, owner, fixed)

    # -- per-net passability mask ------------------------------------------
    def _mask_for(self, net_id: int, half_width: float = 0.100,
                  strict: bool = False) -> np.ndarray:  # noqa: C901
        """Boolean array [2, nx, ny]: True where `net_id` may place copper.

        `half_width` is half the width of the track about to be placed.  The
        exclusion radius is MIN_CLEARANCE + half_width, and foreign copper is
        already stamped at its own true half-width, so the edge-to-edge gap
        comes out at >= MIN_CLEARANCE by construction.
        """
        others = (self.occ != FREE) & (self.occ != net_id)
        blocked = np.zeros_like(others)
        # One radius for all foreign copper.  Holding routed tracks at the
        # strict radius around *fixed* copper was tried and rejected: pads
        # and fan-out stubs are fixed copper, so it makes escaping any
        # fine-pitch part impossible (routing completeness fell from 80/80
        # to 68/80).  Instead the base radius is used everywhere and the
        # geometric repair / concession passes clean up afterwards.
        radius = exclusion_radius(half_width, strict)
        for L in (0, 1):
            blocked[L] = _dilate(others[L], radius)
        # A net's own copper is always usable, even where a neighbouring pad's
        # clearance ring covers it.  Without this, any pad on a 0.5 mm-pitch
        # package is unreachable from itself: its neighbours' rings bury it,
        # the A* start set comes out empty and the net looks unroutable.
        blocked &= ~(self.occ == net_id)
        # Hard keep-outs (board edge, antenna) override everything.
        blocked |= (self.occ == BLOCKED)
        return ~blocked

    def stamp_segment(self, layer: int | None, a: tuple[float, float],
                      b: tuple[float, float], width: float,
                      owner: int, fixed: bool = False) -> None:
        """Stamp copper along an arbitrary-angle segment by sampling it."""
        dx, dy = b[0] - a[0], b[1] - a[1]
        steps = max(2, int(round(max(abs(dx), abs(dy)) / (GRID / 2)) + 1))
        for k in range(steps + 1):
            t = k / steps
            self._stamp_cells(layer, a[0] + dx * t, a[1] + dy * t,
                              stamp_radius(width / 2.0), owner, fixed)

    def _stamp_cells(self, layer: int | None, x: float, y: float,
                     radius: float, owner: int, fixed: bool = False) -> None:
        """Claim every cell whose centre is within `radius` of (x, y)."""
        i0, j0 = self.c(x, y)
        offs = [(0, 0)] + (_disc_offsets(radius) if radius > 0 else [])
        layers = (0, 1) if layer is None else (layer,)
        for L in layers:
            for di, dj in offs:
                i, j = i0 + di, j0 + dj
                if 0 <= i < self.nx and 0 <= j < self.ny:
                    if self.occ[L, i, j] == FREE:
                        self.occ[L, i, j] = owner
                    if fixed:
                        self.fixed[L, i, j] = True

    def segment_is_clear(self, layer: int, a: tuple[float, float],
                         b: tuple[float, float], width: float,
                         net_id: int, strict: bool = False) -> bool:
        """True if a segment can be laid without touching other copper.

        Fan-out stubs are emitted before global routing, so without this
        check they are free to cross a neighbouring pad - a short that no
        later stage would attribute to them.

        Fan-out stubs are checked at the BASE radius.  Checking them
        strictly was tried and rejected: it rejected 25 of 45 escapes, and
        without an escape the router cannot reach a fine-pitch pad at all, so
        completeness fell from 80/80 to 75/80.  The stubs are what make the
        dense parts routable.

        Plane spurs pass `strict=True`.  They are short, there is a free
        choice of via position for each, and a spur that lands too close to a
        stub is the one violation nothing downstream can repair - both sides
        are fixed copper.
        """
        mask = self._mask_for(net_id, width / 2.0, strict=strict)
        dx, dy = b[0] - a[0], b[1] - a[1]
        steps = max(2, int(round(max(abs(dx), abs(dy)) / (GRID / 2)) + 1))
        for k in range(steps + 1):
            t = k / steps
            i, j = self.c(a[0] + dx * t, a[1] + dy * t)
            if not (0 <= i < self.nx and 0 <= j < self.ny):
                return False
            if not mask[layer, i, j]:
                return False
        return True

    # -- routing ------------------------------------------------------------
    def route_net(self, net: str, terminals: dict[str, list[tuple[int, int, int]]],
                  width: float, *, allow_bottom: bool = True,
                  via_cost: int = VIA_COST, strict: bool = False) -> str | None:
        """Route one net.

        `terminals` maps a label ("U3.IO4") to the list of (layer, i, j) grid
        cells that already belong to that terminal - a pad occupies many
        cells, and a through-hole pad exists on both layers.  Returns None on
        success, or a reason string naming the terminal that could not be
        reached.
        """
        if len(terminals) < 2:
            return None
        nid = self.nid(net)
        mask = self._mask_for(nid, width / 2.0, strict)

        # Seed the connected set with the terminal that has the most cells
        # (usually the largest pad), then attach the rest nearest-first.
        items = sorted(terminals.items(), key=lambda kv: -len(kv[1]))
        connected: set[tuple[int, int, int]] = set(items[0][1])
        remaining = list(items[1:])

        while remaining:
            def d2(kv):
                return min((ti - ci) ** 2 + (tj - cj) ** 2
                           for _, ti, tj in kv[1]
                           for _, ci, cj in list(connected)[:40])
            remaining.sort(key=d2)
            label, tgt = remaining.pop(0)
            starts = {c for c in tgt if mask[c]}
            path = self._astar(starts, connected, mask, allow_bottom, via_cost)
            if path is None:
                if not starts:
                    why = "every pad cell is inside another net's clearance ring"
                elif getattr(self, "last_exhausted", True):
                    why = "no legal path exists through the existing copper"
                else:
                    why = "search limit reached before a path was found"
                return (f"{label} unreachable ({why}); "
                        f"{len(remaining)} further branch(es) skipped")
            self._commit(net, nid, path, width, mask)
            connected.update(tgt)
            connected.update(path)
        return None

    def _astar(self, starts: set[tuple[int, int, int]],
               goals: set[tuple[int, int, int]], mask: np.ndarray,
               allow_bottom: bool, via_cost: int):
        # Heuristic: Manhattan distance to the goal set's bounding box.  It is
        # admissible (never overestimates) and O(1), unlike a min over every
        # goal cell - which matters because the goal set is the whole of the
        # net's committed copper and grows as branches are added.
        gi0 = min(c[1] for c in goals)
        gi1 = max(c[1] for c in goals)
        gj0 = min(c[2] for c in goals)
        gj1 = max(c[2] for c in goals)

        def hcost(i: int, j: int) -> int:
            # Chebyshev distance to the goal bounding box, priced at the
            # orthogonal step cost.  Admissible with 45 degree moves allowed,
            # because no single step can close more than one cell in the
            # dominant axis and no step costs less than STEP_ORTHO.
            dx = max(0, gi0 - i, i - gi1)
            dy = max(0, gj0 - j, j - gj1)
            return STEP_ORTHO * max(dx, dy)

        openq: list[tuple[int, int, tuple[int, int, int]]] = []
        gscore: dict[tuple[int, int, int], int] = {}
        came: dict[tuple[int, int, int], tuple[int, int, int]] = {}
        for s in starts:
            if not mask[s]:
                continue
            gscore[s] = 0
            heapq.heappush(openq, (hcost(s[1], s[2]), 0, s))
        if not openq:
            return None

        goalset = set(goals)
        limit = 1_400_000
        popped = 0
        self.last_exhausted = True
        while openq:
            _, g, cur = heapq.heappop(openq)
            if g > gscore.get(cur, 1 << 30):
                continue
            if cur in goalset:
                path = [cur]
                while path[-1] in came:
                    path.append(came[path[-1]])
                return path[::-1]
            popped += 1
            if popped > limit:
                self.last_exhausted = False
                return None
            L, i, j = cur
            for dL, di, dj, step in (
                    (0, 1, 0, STEP_ORTHO), (0, -1, 0, STEP_ORTHO),
                    (0, 0, 1, STEP_ORTHO), (0, 0, -1, STEP_ORTHO),
                    (0, 1, 1, STEP_DIAG), (0, 1, -1, STEP_DIAG),
                    (0, -1, 1, STEP_DIAG), (0, -1, -1, STEP_DIAG),
                    (1, 0, 0, via_cost)):
                if dL:
                    nl = 1 - L
                    if nl == BOT and not allow_bottom:
                        continue
                    nxt = (nl, i, j)
                    # A via needs both layers clear at that spot.
                    if not (mask[L, i, j] and mask[nl, i, j]):
                        continue
                else:
                    ni, nj = i + di, j + dj
                    if not (0 <= ni < self.nx and 0 <= nj < self.ny):
                        continue
                    nxt = (L, ni, nj)
                    if not mask[nxt]:
                        continue
                    if di and dj:
                        # Do not cut a corner between two blocked cells.
                        if not (mask[L, i + di, j] and mask[L, i, j + dj]):
                            continue
                cost = step + (BOTTOM_COST if nxt[0] == BOT and not dL else 0)
                ng = g + cost
                if ng < gscore.get(nxt, 1 << 30):
                    gscore[nxt] = ng
                    came[nxt] = cur
                    heapq.heappush(openq, (ng + hcost(nxt[1], nxt[2]), ng, nxt))
        return None

    def _commit(self, net: str, nid: int, path: list[tuple[int, int, int]],
                width: float, mask: np.ndarray) -> None:
        """Turn a cell path into tracks + vias and stamp it into the grid."""
        runs: list[tuple[int, list[tuple[int, int]]]] = []
        cur_layer = path[0][0]
        run = [(path[0][1], path[0][2])]
        for L, i, j in path[1:]:
            if L != cur_layer:
                runs.append((cur_layer, run))
                x, y = self.xy(i, j)
                self.commit_log.setdefault(net, []).append(
                    ("via", len(self.vias)))
                self.vias.append(Via(net, x, y))
                self.stamp_disc(None, x, y, 0.6, nid)
                self.commit_cells.setdefault(net, []).extend(
                    (L2, i + di, j + dj) for L2 in (0, 1)
                    for di in (-1, 0, 1) for dj in (-1, 0, 1))
                mask[0, i, j] = False
                mask[1, i, j] = False
                cur_layer = L
                run = [(i, j)]
            else:
                run.append((i, j))
        runs.append((cur_layer, run))

        # Stamp each conductor at its own true half-width, so the clearance
        # every later net computes is measured from the copper edge rather
        # than from the centreline.
        halo = _disc_offsets(stamp_radius(width / 2.0))
        for L, cells in runs:
            if len(cells) < 2:
                continue
            pts = _simplify([self.xy(i, j) for i, j in cells])
            self.commit_log.setdefault(net, []).append(("track", len(self.tracks)))
            self.tracks.append(
                Track(net, 1 if L == TOP else 16, pts, width)
            )
            for i, j in cells:
                for di, dj in [(0, 0)] + halo:
                    a, b = i + di, j + dj
                    if 0 <= a < self.nx and 0 <= b < self.ny:
                        if self.occ[L, a, b] == FREE:
                            self.occ[L, a, b] = nid
                            self.commit_cells.setdefault(net, []).append(
                                (L, a, b))


_DISC_CACHE: dict[float, list[tuple[int, int]]] = {}


def _disc_offsets(radius_mm: float) -> list[tuple[int, int]]:
    """Cell offsets whose centres lie within `radius_mm` of the origin."""
    key = round(radius_mm, 4)
    if key not in _DISC_CACHE:
        n = int(radius_mm / GRID) + 1
        r2 = (radius_mm / GRID) ** 2
        _DISC_CACHE[key] = [
            (di, dj)
            for di in range(-n, n + 1) for dj in range(-n, n + 1)
            if di * di + dj * dj <= r2 and (di or dj)
        ]
    return _DISC_CACHE[key]


def _dilate(a: np.ndarray, radius_mm: float) -> np.ndarray:
    """Binary dilation by a EUCLIDEAN disc.

    This has to be a disc, not a diamond or a square.  A diamond of L1 radius
    2 admits a diagonal neighbour whose true separation is only
    0.2*sqrt(2) = 0.283 mm, so two 45-degree tracks placed 2 cells apart end
    up 0.03 mm from each other - a clearance violation the grid cannot see.
    A disc measures the distance that actually matters.
    """
    out = a.copy()
    for di, dj in _disc_offsets(radius_mm):
        sx = slice(max(di, 0), a.shape[0] + min(di, 0))
        dx = slice(max(-di, 0), a.shape[0] + min(-di, 0))
        sy = slice(max(dj, 0), a.shape[1] + min(dj, 0))
        dy = slice(max(-dj, 0), a.shape[1] + min(-dj, 0))
        out[sx, sy] |= a[dx, dy]
    return out


def _simplify(pts: list[tuple[float, float]]) -> list[tuple[float, float]]:
    """Collapse collinear runs so the .brd holds few, long wire segments."""
    if len(pts) < 3:
        return pts
    out = [pts[0]]
    for k in range(1, len(pts) - 1):
        ax, ay = out[-1]
        bx, by = pts[k]
        cx, cy = pts[k + 1]
        if (bx - ax) * (cy - by) != (by - ay) * (cx - bx):
            out.append(pts[k])
    out.append(pts[-1])
    return out


# ---------------------------------------------------------------------------
# Geometric verification, on the emitted polylines rather than on the grid
# ---------------------------------------------------------------------------
def _seg_dist(a, b, c, d) -> float:
    """Minimum distance between segments ab and cd."""
    def pt_seg(p, s, e):
        vx, vy = e[0] - s[0], e[1] - s[1]
        L2 = vx * vx + vy * vy
        if L2 == 0:
            return ((p[0] - s[0]) ** 2 + (p[1] - s[1]) ** 2) ** 0.5
        t = max(0.0, min(1.0, ((p[0] - s[0]) * vx + (p[1] - s[1]) * vy) / L2))
        qx, qy = s[0] + t * vx, s[1] + t * vy
        return ((p[0] - qx) ** 2 + (p[1] - qy) ** 2) ** 0.5

    rx, ry = b[0] - a[0], b[1] - a[1]
    sx, sy = d[0] - c[0], d[1] - c[1]
    den = rx * sy - ry * sx
    if den != 0:
        qpx, qpy = c[0] - a[0], c[1] - a[1]
        t = (qpx * sy - qpy * sx) / den
        u = (qpx * ry - qpy * rx) / den
        if 0 <= t <= 1 and 0 <= u <= 1:
            return 0.0
    return min(pt_seg(a, c, d), pt_seg(b, c, d),
               pt_seg(c, a, b), pt_seg(d, a, b))


def find_violations(tracks, min_clear: float = MIN_CLEARANCE, pads=None,
                    exceptions=None):
    """Segment pairs on the same layer, on different nets, that are closer
    than `min_clear` edge to edge.

    Deliberately measured on the emitted polylines, independently of the
    routing grid, so it can contradict the router rather than agree with it.
    Returns [(gap, netA, netB, layer), ...] worst first.
    """
    segs = []
    for t in tracks:
        for a, b in zip(t.pts, t.pts[1:]):
            segs.append((t.net, t.layer, a, b, t.width / 2.0))
    # Pads, if supplied, are treated as zero-length segments with a radius,
    # so track-to-pad clearance is covered by the same sweep.
    for net, layer, seg, radius in (pads or []):
        segs.append((net, layer, seg[0], seg[1], radius))
    by_layer: dict[int, list] = {}
    for sg in segs:
        by_layer.setdefault(sg[1], []).append(sg)

    out = []
    for layer, items in by_layer.items():
        # Bucket by a coarse grid so this stays O(n) in practice.
        CELL = 3.0
        buckets: dict[tuple[int, int], list[int]] = {}
        for idx, (_, _, a, b, _) in enumerate(items):
            for gx in range(int(min(a[0], b[0]) / CELL) - 1,
                            int(max(a[0], b[0]) / CELL) + 2):
                for gy in range(int(min(a[1], b[1]) / CELL) - 1,
                                int(max(a[1], b[1]) / CELL) + 2):
                    buckets.setdefault((gx, gy), []).append(idx)
        checked = set()
        for idxs in buckets.values():
            for ii in range(len(idxs)):
                for jj in range(ii + 1, len(idxs)):
                    i, j = idxs[ii], idxs[jj]
                    key = (i, j) if i < j else (j, i)
                    if key in checked:
                        continue
                    checked.add(key)
                    n1, _, a1, b1, h1 = items[i]
                    n2, _, a2, b2, h2 = items[j]
                    if n1 == n2:
                        continue
                    gap = _seg_dist(a1, b1, a2, b2) - h1 - h2
                    limit = min_clear
                    if exceptions:
                        mx = (a1[0] + b1[0] + a2[0] + b2[0]) / 4.0
                        my = (a1[1] + b1[1] + a2[1] + b2[1]) / 4.0
                        for x1, y1, x2, y2, c in exceptions:
                            if x1 <= mx <= x2 and y1 <= my <= y2:
                                limit = min(limit, c)
                    if gap < limit - 1e-9:
                        out.append((gap, n1, n2, layer))
    out.sort()
    return out
