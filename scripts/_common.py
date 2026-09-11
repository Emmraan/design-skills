"""Shared helpers for scripts/add.py, update.py, update-all.py, delete.py,
import.py, rebuild.py, validate.py.

Keeps path resolution, JSON I/O, fingerprinting, and the Dembrandt command
template in one place so the scripts stay consistent with each other.
"""
from __future__ import annotations

import hashlib
import json
import re
import subprocess
import sys
from pathlib import Path
from urllib.parse import urlparse

# Print to the console in UTF-8 regardless of the Windows codepage (avoids
# UnicodeEncodeError on em-dashes/arrows in CLI output).
for _stream in (sys.stdout, sys.stderr):
    try:
        _stream.reconfigure(encoding="utf-8")
    except (AttributeError, ValueError):
        pass

REPO_ROOT = Path(__file__).resolve().parent.parent
WEBSITES_DIR = REPO_ROOT / "references" / "websites"
RETRIEVAL_DIR = REPO_ROOT / "references" / "retrieval"
OUTPUT_DIR = REPO_ROOT / "output"

# Dembrandt extraction command template (locked decision D6).
DEMBRANDT_FLAGS = "--save-output --design-md --wcag"
DEMBRANDT_CRAWL = 5


def dembrandt_command(url: str, crawl: int = DEMBRANDT_CRAWL, compare: str | None = None,
                      extra: str = "") -> str:
    """Return the Dembrandt CLI command for <url> as a single string."""
    flags = [DEMBRANDT_FLAGS, f"--crawl {crawl}"]
    if compare:
        flags.append(f"--compare {compare}")
    if extra:
        flags.append(extra)
    return f"npx dembrandt {url} {' '.join(flags)}"


def slugify(url: str) -> str:
    """Derive a default slug from a URL (www prefix + port removed, lowercase).

    e.g. https://example.com/ -> example ; https://www.some-app.io/x -> some-app
    """
    host = urlparse(url).netloc.lower()
    host = re.sub(r"^www\.", "", host)
    if ":" in host:
        host = host.split(":", 1)[0]
    return re.sub(r"[^a-z0-9-]", "", host.split(".")[0])


def read_json(path: Path) -> dict:
    with path.open("r", encoding="utf-8-sig") as fh:
        return json.load(fh)


def write_json(path: Path, data: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as fh:
        json.dump(data, fh, indent=2, ensure_ascii=False)
        fh.write("\n")


def fingerprint(baseline: Path) -> str:
    """Return the SHA1 hex prefix of a baseline.json (fingerprint convention)."""
    digest = hashlib.sha1(baseline.read_bytes()).hexdigest().upper()
    return digest[:12]


def latest_extraction(domain: str) -> Path | None:
    """Newest Dembrandt JSON snapshot under output/<domain>/ if any."""
    dom_dir = OUTPUT_DIR / domain
    if not dom_dir.is_dir():
        return None
    snaps = sorted(dom_dir.glob("*_v*.json"), key=lambda p: p.stat().st_mtime)
    return snaps[-1] if snaps else None


def run_script(name: str) -> int:
    """Run another repo-management script (python scripts/<name>)."""
    return subprocess.call([sys.executable, str(REPO_ROOT / "scripts" / name)])


def out(msg: str) -> None:
    print(msg, file=sys.stdout)


def cleanup_consumed_snapshot(snapshot: str | Path) -> bool:
    """Delete a consumed Dembrandt extraction snapshot after a successful finalize.

    Removes ONLY the given snapshot file, then removes its parent folder when it
    lives directly under OUTPUT_DIR and no other `*_v*.json` snapshots remain in
    it. The snapshot content already lives in the site's baseline.json, so the
    cache file is redundant; leftover folders would only waste disk (low-spec
    machine rule).

    Safety: only files directly under OUTPUT_DIR are ever touched — anything
    outside OUTPUT_DIR is refused. Never raises; returns False (with a warning)
    when there is nothing to do or removal fails. Callers must invoke this ONLY
    after rebuild.py + validate.py both exit 0.
    """
    try:
        snap = Path(snapshot)
        if not snap.is_file():
            print(f"  [warn] snapshot already gone: {snap}")
            return False
        try:
            rel = snap.resolve().relative_to(OUTPUT_DIR.resolve())
        except ValueError:
            print(f"  [warn] refusing to delete outside output/: {snap}")
            return False
        snap.unlink()
        print(f"  cleaned up consumed snapshot: {rel.as_posix()}")
        parent = snap.parent
        if parent.resolve() != OUTPUT_DIR.resolve():
            remaining = sorted(parent.glob("*_v*.json"))
            if not remaining:
                import shutil

                shutil.rmtree(parent)
                print(f"  removed empty extraction folder: {parent.name}/")
        return True
    except OSError as exc:
        print(f"  [warn] could not remove snapshot {snapshot}: {exc}")
        return False
