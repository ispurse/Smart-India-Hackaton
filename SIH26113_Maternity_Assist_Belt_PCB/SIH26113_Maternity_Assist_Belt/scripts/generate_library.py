"""
generate_library.py - Emit SIH26113_Maternity_Assist_Belt.lbr and self-check it.

Run:  python scripts/generate_library.py
"""

from __future__ import annotations

import pathlib
import sys
import xml.etree.ElementTree as ET

sys.path.insert(0, str(pathlib.Path(__file__).parent))

from eagle_common import Pad, Pin, Smd, document, library_body  # noqa: F401  # noqa: E402
from lib_defs import (  # noqa: E402
    DEVICESETS,
    LIBRARY_DESCRIPTION,
    LIBRARY_NAME,
    PACKAGES,
    SYMBOLS,
)

ROOT = pathlib.Path(__file__).resolve().parent.parent
OUT = ROOT / "libraries" / f"{LIBRARY_NAME}.lbr"


def check() -> list[str]:
    """Cross-check the library model before writing it out.

    This is the library half of ERC: every deviceset must map every symbol pin
    to a pad that actually exists in the referenced package, and must not
    leave pads unclaimed.
    """
    errs: list[str] = []
    pkgs = {p.name: p for p in PACKAGES}
    syms = {s.name: s for s in SYMBOLS}

    if len(pkgs) != len(PACKAGES):
        errs.append("duplicate package name(s)")
    if len(syms) != len(SYMBOLS):
        errs.append("duplicate symbol name(s)")

    seen: set[str] = set()
    for ds in DEVICESETS:
        if ds.name in seen:
            errs.append(f"{ds.name}: duplicate deviceset name")
        seen.add(ds.name)

        if ds.symbol not in syms:
            errs.append(f"{ds.name}: symbol {ds.symbol!r} not in library")
            continue
        sym_pins = set(syms[ds.symbol].pin_names())

        if ds.package is None:
            if ds.connects:
                errs.append(f"{ds.name}: package-less device has connects")
            continue
        if ds.package not in pkgs:
            errs.append(f"{ds.name}: package {ds.package!r} not in library")
            continue
        pads = set(pkgs[ds.package].pad_names())

        mapped_pins = set(ds.connects)
        missing = sym_pins - mapped_pins
        if missing:
            errs.append(f"{ds.name}: symbol pins not connected: {sorted(missing)}")
        extra = mapped_pins - sym_pins
        if extra:
            errs.append(f"{ds.name}: connects reference unknown pins: {sorted(extra)}")

        # A pin may claim several pads via EAGLE's space-separated pad list
        # (e.g. the internally-bonded lead pairs of a tactile switch).
        claimed: set[str] = set()
        for padspec in ds.connects.values():
            claimed.update(padspec.split())
        bad_pads = sorted(claimed - pads)
        if bad_pads:
            errs.append(f"{ds.name}: connects reference unknown pads: {bad_pads}")

        orphan = pads - claimed
        if orphan:
            errs.append(f"{ds.name}: package pads with no symbol pin: {sorted(orphan)}")

    # Every package pad name must be unique inside that package.
    for p in PACKAGES:
        names = p.pad_names()
        if len(names) != len(set(names)):
            errs.append(f"package {p.name}: duplicate pad name(s)")

    # Every symbol pin name must be unique inside that symbol.
    for s in SYMBOLS:
        names = s.pin_names()
        if len(names) != len(set(names)):
            errs.append(f"symbol {s.name}: duplicate pin name(s)")

    # No two pads of a package may overlap, and they must keep a real gap.
    # This exists because it caught a live defect: a SOT-23-5 land pattern
    # with its radial and tangential dimensions transposed put 1.10 mm pads
    # on a 0.95 mm pitch, overlapping adjacent pins by 0.15 mm.  On the
    # AP2112K that is a short from VIN to GND, and it looks entirely
    # plausible in the library editor.
    MIN_PAD_GAP = 0.15
    for p in PACKAGES:
        pads = [i for i in p.items if isinstance(i, (Smd, Pad))]
        for a in range(len(pads)):
            for b in range(a + 1, len(pads)):
                p1, p2 = pads[a], pads[b]
                w1, h1 = _pad_size(p1)
                w2, h2 = _pad_size(p2)
                gx = abs(p1.x - p2.x) - (w1 + w2) / 2
                gy = abs(p1.y - p2.y) - (h1 + h2) / 2
                gap = max(gx, gy)
                if gap < 0:
                    errs.append(
                        f"package {p.name}: pads {p1.name} and {p2.name} "
                        f"OVERLAP by {abs(gap):.3f} mm")
                elif gap < MIN_PAD_GAP and not _is_thermal(p, p1, p2):
                    errs.append(
                        f"package {p.name}: pads {p1.name} and {p2.name} are "
                        f"only {gap:.3f} mm apart (min {MIN_PAD_GAP} mm)")

    return errs


def _pad_size(pd):
    if isinstance(pd, Pad):
        d = pd.diameter or pd.drill * 1.8
        return d, d
    dx, dy = pd.dx, pd.dy
    if pd.rot in ("R90", "R270"):
        dx, dy = dy, dx
    return dx, dy


def _is_thermal(pkg, p1, p2) -> bool:
    """Exposed/thermal pads legitimately sit close to the signal pads."""
    THERMAL = {"41", "EP", "7"}
    return p1.name in THERMAL or p2.name in THERMAL


def main() -> int:
    errs = check()
    if errs:
        print("LIBRARY MODEL ERRORS:")
        for e in errs:
            print("  -", e)
        return 1

    xml = document(
        library_body(LIBRARY_DESCRIPTION, PACKAGES, SYMBOLS, DEVICESETS)
    )
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(xml, encoding="utf-8")

    # Structural XML check (the DTD is not shipped with EAGLE files, so we
    # verify well-formedness plus the element counts we expect).
    tree = ET.fromstring(xml.split("\n", 2)[2])
    lib = tree.find("./drawing/library")
    npk = len(lib.findall("./packages/package"))
    nsy = len(lib.findall("./symbols/symbol"))
    nds = len(lib.findall("./devicesets/deviceset"))
    npad = len(lib.findall(".//package/pad")) + len(lib.findall(".//package/smd"))
    npin = len(lib.findall(".//symbol/pin"))

    print(f"WROTE {OUT.relative_to(ROOT)}  ({OUT.stat().st_size:,} bytes)")
    print(f"  packages={npk}  symbols={nsy}  devicesets={nds}")
    print(f"  total pads/smds={npad}  total symbol pins={npin}")
    assert npk == len(PACKAGES) and nsy == len(SYMBOLS) and nds == len(DEVICESETS)
    print("  library model self-check: PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
