"""
make_fusion_project.py - assemble a single folder that Fusion / EAGLE can open
as one linked project.

WHY THIS EXISTS
---------------
EAGLE and Fusion Electronics pair a schematic with a board **by filename and
directory**: opening `foo.brd` makes EAGLE look for `foo.sch` in the *same*
folder.  There is no link stored inside either file.

This repository keeps them apart for legibility - `schematic/` and `pcb/` -
which means that if you open either one straight from its own folder, Fusion
loads it *standalone*.  The files themselves are fine, but:

  * the schematic <-> board consistency check cannot run;
  * forward / back annotation is off, so an edit in one is not reflected in
    the other;
  * EAGLE may warn that the board and schematic will become inconsistent.

So this script copies the three files into one flat directory with a shared
base name.  Open THAT folder in Fusion.

It is a copy, not a move: `schematic/` and `pcb/` remain the canonical output
of the generators.  Re-run this script after any regeneration.

Run:  python scripts/make_fusion_project.py
"""

from __future__ import annotations

import pathlib
import shutil

ROOT = pathlib.Path(__file__).resolve().parent.parent
NAME = "SIH26113_Maternity_Assist_Belt"
OUT = ROOT / "fusion_project"

SOURCES = [
    ROOT / "libraries" / f"{NAME}.lbr",
    ROOT / "schematic" / f"{NAME}.sch",
    ROOT / "pcb" / f"{NAME}.brd",
]

README = f"""# Open this folder in Autodesk Fusion

These three files are **copies**. The canonical versions live in
`../libraries/`, `../schematic/` and `../pcb/`, which is what the generators
in `../scripts/` write.

They are gathered here because **EAGLE and Fusion pair a schematic with a
board by filename and directory** - opening `{NAME}.brd`
makes the tool look for `{NAME}.sch` alongside it. Split
across two folders, each file opens standalone and the schematic/board
consistency check and forward-annotation do not work.

## What to do

1. Open `{NAME}.sch` from **this** folder.
2. Fusion will find the matching `.brd` automatically.
3. Follow `../documentation/PCB_BUILD_GUIDE.md`, or Part 19 of
   `../FULL_INSTRUCTION_TUTORIAL.md`.

## Before you power anything

Read `../documentation/REQUIRES_CONFIRMATION.md`. Three items there are
BLOCKING and one of them is a fire risk.

## Regenerating

Re-run `python scripts/make_fusion_project.py` after any regeneration, or
just run `python scripts/build_all.py`, which does it as its last step.

**Once you start editing in Fusion, these copies become the authoritative
version** and re-running the generators will overwrite them. See section 18.7
("the fork problem") of the tutorial.
"""


def main() -> int:
    missing = [p for p in SOURCES if not p.exists()]
    if missing:
        for p in missing:
            print(f"  MISSING: {p.relative_to(ROOT)}")
        print("Run scripts/build_all.py first.")
        return 1

    OUT.mkdir(exist_ok=True)
    for src in SOURCES:
        dst = OUT / src.name
        shutil.copy2(src, dst)
        print(f"  {src.relative_to(ROOT)}  ->  {dst.relative_to(ROOT)}")

    (OUT / "README.md").write_text(README, encoding="utf-8")
    print(f"  wrote {(OUT / 'README.md').relative_to(ROOT)}")
    print(f"\nOpen  fusion_project/{NAME}.sch  in Fusion.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
