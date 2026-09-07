"""
geom.py - Symbol/package pin geometry and instance transforms.

Shared by the schematic generator, the board generator, the routers and the
renderers so that "where is pin X of part Y" has exactly one answer.
"""

from __future__ import annotations

import math
import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).parent))

from eagle_common import Pad, Pin, Smd  # noqa: E402
from lib_defs import DEVICESETS, PACKAGES, SYMBOLS  # noqa: E402

SYM = {s.name: s for s in SYMBOLS}
PKG = {p.name: p for p in PACKAGES}
DS = {d.name: d for d in DEVICESETS}

ROT = {"R0": 0.0, "R90": 90.0, "R180": 180.0, "R270": 270.0}


def rotate(x: float, y: float, rot: str) -> tuple[float, float]:
    a = math.radians(ROT[rot])
    c, s = math.cos(a), math.sin(a)
    return (x * c - y * s, x * s + y * c)


def add_rot(a: str, b: str) -> str:
    return f"R{int((ROT[a] + ROT[b]) % 360)}"


# Direction the free end of a pin points, given the pin's own rotation.
# A pin with rot=R0 has its body extending in +x, so its connection point is
# the leftmost end and any stub must continue in -x.
_STUB = {"R0": (-1.0, 0.0), "R90": (0.0, -1.0), "R180": (1.0, 0.0),
         "R270": (0.0, 1.0)}


def symbol_pins(deviceset: str) -> dict[str, Pin]:
    ds = DS[deviceset]
    return {i.name: i for i in SYM[ds.symbol].items if isinstance(i, Pin)}


def sch_pin_pos(deviceset: str, pin: str, ix: float, iy: float,
                irot: str) -> tuple[float, float, tuple[float, float]]:
    """Absolute schematic position of a pin plus its outward stub direction."""
    p = symbol_pins(deviceset)[pin]
    px, py = rotate(p.x, p.y, irot)
    sdx, sdy = _STUB[p.rot]
    rdx, rdy = rotate(sdx, sdy, irot)
    return ix + px, iy + py, (round(rdx, 6), round(rdy, 6))


def package_pads(package: str) -> dict[str, Pad | Smd]:
    return {i.name: i for i in PKG[package].items if isinstance(i, (Pad, Smd))}


def pad_of(deviceset: str, pin: str) -> list[str]:
    """Pads that a symbol pin maps to (EAGLE allows a space-separated list)."""
    return DS[deviceset].connects[pin].split()


def brd_pad_pos(deviceset: str, pin: str, ex: float, ey: float,
                erot: str) -> list[tuple[str, float, float, bool]]:
    """Absolute board positions of the pad(s) behind a symbol pin.

    Returns [(pad_name, x, y, is_through_hole), ...].
    """
    ds = DS[deviceset]
    pads = package_pads(ds.package)
    out = []
    for pname in pad_of(deviceset, pin):
        pd = pads[pname]
        px, py = rotate(pd.x, pd.y, erot)
        out.append((pname, ex + px, ey + py, isinstance(pd, Pad)))
    return out


def pad_extent(deviceset: str, pad_name: str,
               erot: str) -> tuple[float, float, bool]:
    """(width, height) of a pad in board axes, and whether it is through-hole."""
    ds = DS[deviceset]
    pd = package_pads(ds.package)[pad_name]
    if isinstance(pd, Pad):
        d = pd.diameter or pd.drill * 1.8
        return d, d, True
    dx, dy = pd.dx, pd.dy
    if pd.rot in ("R90", "R270"):
        dx, dy = dy, dx
    if erot in ("R90", "R270"):
        dx, dy = dy, dx
    return dx, dy, False


def all_pads_of_part(deviceset: str) -> list[str]:
    ds = DS[deviceset]
    if ds.package is None:
        return []
    return list(package_pads(ds.package))
