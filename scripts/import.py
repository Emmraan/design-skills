"""Import a manually prepared website folder.

Flow:
  1. Detect the folder type:
       - Structured template folder (metadata.json + analysis.md) -> copy as-is, fix
         slug to the folder name.
       - Woblo export (index.html + css/ + assets/) -> read the real source: pick the
         <title> and og:url for metadata, keep the HTML/CSS so the agent can do a deep
         analysis, and scaffold a draft analysis.md.
  2. Copy it into references/websites/<slug>/.
  3. Run rebuild.py + validate.py.

Usage:
    python scripts/import.py <folder> [--slug <slug>]
"""
from __future__ import annotations

import argparse
import datetime as dt
import re
import shutil
import sys
from pathlib import Path

from _common import WEBSITES_DIR, read_json, run_script, write_json


def is_woblo(folder: Path) -> bool:
    return (folder / "index.html").exists() and (folder / "css").exists()


def slug_from_url(url: str) -> str:
    m = re.search(r"https?://(?:www\.)?([^/]+)", url)
    if not m:
        return "site"
    host = m.group(1)
    return host.split(".")[-2] if host.count(".") >= 2 else host.split(".")[0]


def title_from_html(index_html: Path) -> str:
    text = index_html.read_text(encoding="utf-8", errors="replace")
    m = re.search(r"<title[^>]*>(.*?)</title>", text, re.S)
    return (m.group(1).strip() or "Site") if m else "Site"


def url_from_html(index_html: Path) -> str | None:
    text = index_html.read_text(encoding="utf-8", errors="replace")
    for m in re.finditer(r'property="og:url"\s+content="([^"]+)"', text):
        return m.group(1)
    for m in re.finditer(r'name="twitter:url"\s+content="([^"]+)"', text):
        return m.group(1)
    return None


def main() -> None:
    parser = argparse.ArgumentParser(description="Import a prepared website folder.")
    parser.add_argument("folder", help="Path to the folder to import")
    parser.add_argument("--slug", help="Override derived slug")
    args = parser.parse_args()

    src = Path(args.folder)
    if not src.is_dir():
        sys.exit(f"error: folder not found: {src}")

    # --- structured template folder ---------------------------------------
    if (src / "metadata.json").exists():
        meta = read_json(src / "metadata.json")
        slug = args.slug or meta.get("slug") or slug_from_url(meta.get("source-url", ""))
        dest = WEBSITES_DIR / slug
        dest.mkdir(parents=True, exist_ok=True)
        meta["slug"] = slug
        if not (src / "baseline.json").exists():
            # No baseline copied -> keep validate.py happy: mark fingerprint pending
            meta["fingerprint"] = "pending"
        write_json(dest / "metadata.json", meta)
        for name in ("analysis.md", "baseline.json"):
            if (src / name).exists():
                shutil.copy2(src / name, dest / name)
        print(f"imported structured folder as references/websites/{slug}/")
    # --- Woblo export -----------------------------------------------------
    elif is_woblo(src):
        index_html = src / "index.html"
        url = url_from_html(index_html) or f"file://{src}"
        slug = args.slug or slug_from_url(url)
        dest = WEBSITES_DIR / slug
        dest.mkdir(parents=True, exist_ok=True)
        shutil.copytree(src, dest / "source", dirs_exist_ok=True)
        write_json(dest / "metadata.json", {
            "slug": slug,
            "name": title_from_html(index_html),
            "source-url": url,
            "industry": "tbd",
            "style": "tbd",
            "layout": "tbd",
            "theme": "tbd",
            "complexity": "medium",
            "cta": "tbd",
            "responsive": True,
            "collected-at": dt.date.today().isoformat(),
            "collected-by": "woblo",
            "baseline-ref": "baseline.json",
            "fingerprint": "pending",
        })
        draft = (WEBSITES_DIR / "_template" / "analysis.md").read_text(encoding="utf-8")
        draft = f"# {slug.title()} — Design Analysis\n\n" + \
            f"> Source: `{url}` (Woblo export) · Deep analysis from real HTML/CSS in " \
            f"`source/`\n>\n" + \
            f"> Analyze `source/index.html` + `source/css/` directly — exact components, " \
            f"breakpoints, values.\n>\n" + draft
        (dest / "analysis.md").write_text(draft, encoding="utf-8")
        print(f"imported Woblo export as references/websites/{slug}/")
        print(f"  real source copied to references/websites/{slug}/source/")
        print("  -> complete analysis.md from the real source (see analyze-agent.md)")
    else:
        sys.exit("error: not a structured folder (metadata.json) nor a Woblo export "
                 "(index.html + css/)")

    for name in ("rebuild.py", "validate.py"):
        run_script(name)


if __name__ == "__main__":
    main()
