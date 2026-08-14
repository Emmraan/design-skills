"""Delete a website from the knowledge base.

Flow:
  1. Remove references/websites/<slug>/.
  2. Run rebuild.py to regenerate INDEX.md + retrieval indexes, then validate.py.

Usage:
    python scripts/delete.py <slug>
"""
from __future__ import annotations

import argparse
import shutil
import sys

from _common import WEBSITES_DIR, run_script


def main() -> None:
    parser = argparse.ArgumentParser(description="Delete a website folder.")
    parser.add_argument("slug", help="Website slug under references/websites/")
    args = parser.parse_args()

    folder = WEBSITES_DIR / args.slug
    if not folder.is_dir():
        sys.exit(f"error: no such website folder: {folder}")
    if args.slug.startswith("_"):
        sys.exit("error: refusing to delete a reserved folder (_template)")
    shutil.rmtree(folder)
    print(f"deleted references/websites/{args.slug}/")
    for name in ("rebuild.py", "validate.py"):
        run_script(name)


if __name__ == "__main__":
    main()
