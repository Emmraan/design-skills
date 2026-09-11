"""Update a website when the original site changed.

Flow:
  1. Re-run Dembrandt extraction on the site URL with --compare against the stored
     baseline.json; user runs the command (one instance at a time, low-spec machine).
  2. If drift is detected, Dembrandt exits non-zero and the agent revises the affected
     parts of analysis.md.
  3. Accept the new snapshot with --finalize <json> to replace baseline.json and refresh
     the fingerprint (do this AFTER the agent revises analysis.md).
   4. rebuild.py + validate.py run automatically on finalize; on success the
      consumed snapshot is deleted from output/.

Usage:
    python scripts/update.py <slug>
    python scripts/update.py <slug> --finalize <path-to-new-json>
"""
from __future__ import annotations

import argparse
import datetime as dt
import sys
from pathlib import Path

from _common import WEBSITES_DIR, cleanup_consumed_snapshot, dembrandt_command, \
    fingerprint, read_json, run_script, write_json


def main() -> None:
    parser = argparse.ArgumentParser(description="Update a website after drift.")
    parser.add_argument("slug", help="Website slug under references/websites/")
    parser.add_argument("--finalize", metavar="JSON", default=None,
                        help="Accept a new extraction as the updated baseline")
    args = parser.parse_args()

    folder = WEBSITES_DIR / args.slug
    if not folder.is_dir():
        sys.exit(f"error: no such website folder: {folder}")
    baseline = folder / "baseline.json"
    meta_path = folder / "metadata.json"
    if not baseline.exists() or not meta_path.exists():
        sys.exit(f"error: {args.slug} missing baseline.json or metadata.json")

    meta = read_json(meta_path)
    url = meta["source-url"]

    if args.finalize is None:
        print(f"update: {args.slug} ({url})")
        print("Run Dembrandt to drift-check (you run it — one instance at a time):")
        print(f"\n    {dembrandt_command(url, crawl=5, compare=str(baseline))}\n")
        print("If drift is reported (exit code 1), revise the affected parts of "
              f"{folder / 'analysis.md'} first.")
        print("Then accept the new snapshot:")
        print(f"    python scripts/update.py {args.slug} --finalize <new-json>\n")
        sys.exit(0)

    src = Path(args.finalize)
    if not src.exists():
        sys.exit(f"error: new extraction not found: {src}")
    baseline.write_bytes(src.read_bytes())
    meta["collected-at"] = dt.date.today().isoformat()
    meta["fingerprint"] = fingerprint(baseline)
    write_json(meta_path, meta)
    print(f"updated {args.slug}: baseline.json + fingerprint {meta['fingerprint']}")
    results = [run_script(name) for name in ("rebuild.py", "validate.py")]
    if all(rc == 0 for rc in results):
        cleanup_consumed_snapshot(src)
    else:
        print("  [warn] rebuild/validate failed — snapshot left in place, fix first")


if __name__ == "__main__":
    main()
