"""Bulk freshness check for all websites.

Prints the drift-check command for every website that has a baseline.json, one at a
time (the user runs each command on a low-spec machine — never parallel Dembrandt).
Reports which sites have a pending fingerprint in metadata.json.

Usage:
    python scripts/update-all.py
"""
from __future__ import annotations

import sys

from _common import WEBSITES_DIR, dembrandt_command, read_json


def main() -> None:
    folders = sorted(d for d in WEBSITES_DIR.iterdir()
                     if d.is_dir() and not d.name.startswith("_"))
    pending = []
    print(f"update-all: {len(folders)} website(s) with baseline check:\n")
    for folder in folders:
        baseline = folder / "baseline.json"
        meta_path = folder / "metadata.json"
        if not baseline.exists():
            print(f"  {folder.name}: no baseline.json — nothing to check")
            continue
        meta = read_json(meta_path) if meta_path.exists() else {}
        if meta.get("fingerprint") == "pending":
            pending.append(folder.name)
        print(f"  --- {folder.name} ({meta.get('source-url', '?' )}) ---")
        print(f"      {dembrandt_command(meta.get('source-url', ''), crawl=5, compare=str(baseline))}")
    if pending:
        print("\nNote: these still have fingerprint 'pending' (run add.py --finalize or "
              "update.py --finalize):")
        for s in pending:
            print(f"  - {s}")


if __name__ == "__main__":
    main()
    sys.exit(0)
