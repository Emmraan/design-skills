"""Add a website from a URL into the knowledge base.

Flow:
  1. Scaffold references/websites/<slug>/ with metadata.json + a draft analysis.md.
  2. Print the Dembrandt extraction command for the user to run (user runs it on a
     low-spec machine — one at a time; see AGENTS.md D6):
       npx dembrandt <url> --save-output --design-md --wcag --crawl 5
  3. After the user runs it, finalize with the produced JSON:
       python scripts/add.py <url> --finalize output/<domain>/<ts>_v0.28.0.json
      This stores baseline.json, computes the fingerprint, fills metadata, then runs
      rebuild.py + validate.py. On success the consumed snapshot is deleted from
      output/ (its content already lives in baseline.json).

Usage:
    python scripts/add.py <url> [--slug <slug>] [--crawl <n>]
    python scripts/add.py <url> --finalize <path-to-json> [--slug <slug>]
"""
from __future__ import annotations

import argparse
import datetime as dt
import sys
from pathlib import Path

from _common import OUTPUT_DIR, WEBSITES_DIR, cleanup_consumed_snapshot, \
    dembrandt_command, fingerprint, read_json, run_script, slugify, write_json

TEMPLATE_META = WEBSITES_DIR / "_template" / "metadata.json"
TEMPLATE_ANALYSIS = WEBSITES_DIR / "_template" / "analysis.md"


def scaffold(url: str, slug: str) -> None:
    folder = WEBSITES_DIR / slug
    if folder.exists():
        sys.exit(f"error: folder already exists: {folder}")
    folder.mkdir(parents=True)
    meta = read_json(TEMPLATE_META)
    meta.update({
        "slug": slug,
        "source-url": url,
        "collected-at": dt.date.today().isoformat(),
        "fingerprint": "pending",
    })
    write_json(folder / "metadata.json", meta)
    draft = TEMPLATE_ANALYSIS.read_text(encoding="utf-8")
    draft = f"# {slug.title()} — Design Analysis\n\n" + \
        f"> Source: `{url}` · Baseline: `baseline.json` · Collected: " \
        f"{dt.date.today().isoformat()} (Dembrandt)\n>\n" + \
        "> Complete this draft after extraction (see `scripts/analyze-agent.md`):\n>\n" + \
        draft
    (folder / "analysis.md").write_text(draft, encoding="utf-8")
    print(f"scaffolded {folder}/")
    print(f"  - metadata.json (fingerprint pending — finalize to fill it)")
    print(f"  - analysis.md (draft — complete after extraction)")


def finalize(url: str, slug: str, baseline_json: str, crawl: int) -> None:
    folder = WEBSITES_DIR / slug
    if not folder.exists():
        scaffold(url, slug)
    src = Path(baseline_json)
    if not src.exists():
        sys.exit(f"error: extraction JSON not found: {src}")
    dest = folder / "baseline.json"
    dest.write_bytes(src.read_bytes())
    meta = read_json(folder / "metadata.json")
    meta["collected-at"] = dt.date.today().isoformat()
    meta["fingerprint"] = fingerprint(dest)
    write_json(folder / "metadata.json", meta)
    print(f"finalized {slug}: baseline.json + fingerprint {meta['fingerprint']}")
    print(f"  complete analysis.md ({folder / 'analysis.md'}), then:")
    results = [run_script(name) for name in ("rebuild.py", "validate.py")]
    if all(rc == 0 for rc in results):
        cleanup_consumed_snapshot(src)
    else:
        print("  [warn] rebuild/validate failed — snapshot left in place, fix first")


def main() -> None:
    parser = argparse.ArgumentParser(description="Add a website into the knowledge base.")
    parser.add_argument("url", help="Site URL, e.g. https://example.com")
    parser.add_argument("--slug", help="Override derived slug")
    parser.add_argument("--crawl", type=int, default=5, help="Dembrandt crawl depth")
    parser.add_argument("--finalize", metavar="JSON", nargs="?",
                        const="__auto__", default=None,
                        help="Finalize with an extraction JSON (auto = latest in output/)")
    args = parser.parse_args()

    slug = args.slug or slugify(args.url)
    if args.finalize is None:
        scaffold(args.url, slug)
        domain = slug  # best-effort hint; output folder uses the real domain
        print("\nRun Dembrandt next (you run it — one instance at a time on this machine):")
        print(f"\n    {dembrandt_command(args.url, crawl=args.crawl)}\n")
        print("Then finalize with the produced JSON:")
        print(f"    python scripts/add.py {args.url} --finalize output/<domain>/<ts>_v0.28.0.json\n")
        print("(or: python scripts/add.py {url} --finalize  -> auto-picks the newest "
              f"JSON under output/<domain>/)")
        sys.exit(0)

    if args.finalize == "__auto__":
        import re
        dom = __import__("urllib.parse", fromlist=["urlparse"]).urlparse(args.url).netloc
        dom = re.sub(r"^www\.", "", dom)
        cands = sorted((OUTPUT_DIR / dom).glob("*_v*.json"),
                       key=lambda p: p.stat().st_mtime)
        if not cands:
            sys.exit(f"error: no extraction JSON found under {OUTPUT_DIR / dom}")
        chosen = cands[-1]
        print(f"auto-picked extraction: {chosen}")
        finalize(args.url, slug, str(chosen), args.crawl)
    else:
        finalize(args.url, slug, args.finalize, args.crawl)


if __name__ == "__main__":
    main()
