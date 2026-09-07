"""
build_all.py - Regenerate the whole project from scripts/design.py.

Order matters: the library must be valid before the schematic can reference
it, ERC must pass before a board is worth routing, and the documents read the
route/DRC reports that the board and DRC steps write.

Run:  python scripts/build_all.py [--fast]
      --fast  route with a single ordering instead of searching several
"""

from __future__ import annotations

import os
import pathlib
import subprocess
import sys
import time

ROOT = pathlib.Path(__file__).resolve().parent
STEPS = [
    ("library", "generate_library.py", True),
    ("ERC", "validate_erc.py", True),
    ("schematic", "generate_schematic.py", True),
    ("board (place + route)", "generate_board.py", True),
    ("DRC", "validate_drc.py", False),      # airwires are reported, not fatal
    ("plane integrity", "validate_planes.py", False),
    ("renders", "render.py", False),
    ("documents", "generate_docs.py", True),
    ("reports", "gen_reports.py", True),
    ("fusion project folder", "make_fusion_project.py", True),
]


def main() -> int:
    env = dict(os.environ)
    if "--fast" in sys.argv:
        env["SIH_ROUTE_ATTEMPTS"] = "1"
    failures = []
    t0 = time.time()
    for label, script, fatal in STEPS:
        print(f"\n{'=' * 70}\n>>> {label}  ({script})\n{'=' * 70}")
        r = subprocess.run([sys.executable, str(ROOT / script)], env=env)
        if r.returncode != 0:
            if fatal:
                print(f"\n!!! {label} FAILED - stopping.")
                return r.returncode
            failures.append(label)
            print(f"\n--- {label} reported findings (non-fatal, see its "
                  f"report) ---")
    print(f"\n{'=' * 70}")
    print(f"build finished in {time.time() - t0:.0f}s")
    if failures:
        print(f"steps with findings to review: {', '.join(failures)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
