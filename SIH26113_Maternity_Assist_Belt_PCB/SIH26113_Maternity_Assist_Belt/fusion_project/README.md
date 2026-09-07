# Open this folder in Autodesk Fusion

These three files are **copies**. The canonical versions live in
`../libraries/`, `../schematic/` and `../pcb/`, which is what the generators
in `../scripts/` write.

They are gathered here because **EAGLE and Fusion pair a schematic with a
board by filename and directory** - opening `SIH26113_Maternity_Assist_Belt.brd`
makes the tool look for `SIH26113_Maternity_Assist_Belt.sch` alongside it. Split
across two folders, each file opens standalone and the schematic/board
consistency check and forward-annotation do not work.

## What to do

1. Open `SIH26113_Maternity_Assist_Belt.sch` from **this** folder.
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
