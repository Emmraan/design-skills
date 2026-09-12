"""Validate the design-skills repository.

Checks:
  - SKILL.md frontmatter (name matches repo, description present and within length).
  - All relative links in *.md resolve to real files.
  - Every website folder has metadata.json + analysis.md + baseline.json (valid JSON,
    slug matches folder, required metadata fields present, fingerprint matches baseline).
  - references/retrieval/*.json are consistent with references/websites/.
  - references/collections/*.md reference only known website slugs.
  - INDEX.md Websites table matches references/websites/ (no stale/missing slugs).

Usage:
    python scripts/validate.py
"""
from __future__ import annotations

import hashlib
import json
import re
import sys
from pathlib import Path

import yaml

from _common import REPO_ROOT, RETRIEVAL_DIR, WEBSITES_DIR, fingerprint

FAILURES: list[str] = []


def fail(msg: str) -> None:
    FAILURES.append(msg)


def ok(msg: str) -> None:
    print(f"  ok   {msg}")


def check(cond: bool, msg: str) -> None:
    if cond:
        ok(msg)
    else:
        fail(msg)


# ---------------------------------------------------------------- SKILL.md

def validate_skill_md() -> None:
    path = REPO_ROOT / "SKILL.md"
    if not path.exists():
        fail("SKILL.md missing")
        return
    text = path.read_text(encoding="utf-8")
    front = re.match(r"^---\n(.*?)\n---", text, re.S)
    if not front:
        fail("SKILL.md has no YAML frontmatter")
        return
    try:
        meta = yaml.safe_load(front.group(1)) or {}
    except Exception as exc:  # noqa: BLE001
        fail(f"SKILL.md frontmatter invalid: {exc}")
        return
    check(meta.get("name") == "design-skills", "SKILL.md frontmatter: name == 'design-skills'")
    desc = meta.get("description", "")
    check(bool(desc), "SKILL.md frontmatter: description present")
    if desc:
        check(len(desc) <= 1024, f"SKILL.md description length {len(desc)} <= 1024")


# ------------------------------------------------------------------- links

LINK_RE = re.compile(r"\[[^\]]*\]\(([^)]+)\)")
CODE_RE = re.compile(r"`[^`]*`|```.*?```", re.S)


def validate_md_links() -> None:
    checked = 0
    for md in REPO_ROOT.rglob("*.md"):
        if ".git" in md.parts:
            continue
        text = md.read_text(encoding="utf-8")
        plain = CODE_RE.sub(" ", text)
        for target in LINK_RE.findall(plain):
            target = target.strip().split(" ")[0]
            if not target or target.startswith(("http://", "https://", "#", "mailto:")):
                continue
            # strip anchor within the same file
            link_path = target.split("#", 1)[0]
            resolved = (md.parent / link_path).resolve()
            rel = resolved.relative_to(REPO_ROOT.resolve())
            if not resolved.exists():
                fail(f"broken link in {md.relative_to(REPO_ROOT)}: {target}")
            else:
                checked += 1
    ok(f"{checked} relative links resolve")


# --------------------------------------------------------------- websites

REQUIRED_META = ["slug", "name", "source-url", "industry", "style", "layout",
                 "theme", "complexity", "cta", "responsive", "collected-at",
                 "collected-by", "baseline-ref", "fingerprint"]


def validate_websites() -> None:
    folders = [d for d in sorted(WEBSITES_DIR.iterdir())
               if d.is_dir() and not d.name.startswith("_")]
    check(len(folders) >= 1, f"{len(folders)} website folder(s) present")
    for folder in folders:
        slug = folder.name
        meta_path = folder / "metadata.json"
        base_path = folder / "baseline.json"
        ana_path = folder / "analysis.md"

        if not meta_path.exists():
            fail(f"{slug}: missing metadata.json")
        else:
            try:
                meta = json.loads(meta_path.read_text(encoding="utf-8-sig"))
            except Exception as exc:  # noqa: BLE001
                fail(f"{slug}: metadata.json invalid JSON ({exc})")
                meta = {}
            if meta.get("slug") != slug:
                fail(f"{slug}: metadata.slug '{meta.get('slug')}' != folder name")
            for field in REQUIRED_META:
                if field not in meta:
                    fail(f"{slug}: metadata missing field '{field}'")

        if not ana_path.exists():
            fail(f"{slug}: missing analysis.md")

        pending = meta.get("fingerprint") == "pending"
        if base_path.exists():
            try:
                json.loads(base_path.read_text(encoding="utf-8-sig"))
            except Exception as exc:  # noqa: BLE001
                fail(f"{slug}: baseline.json invalid JSON ({exc})")
        if pending:
            # Scaffolded/imported but not finalized yet — baseline not required.
            continue
        if not base_path.exists():
            fail(f"{slug}: fingerprint set but baseline.json missing")
            continue
        fp = fingerprint(base_path)
        if meta.get("fingerprint") != fp:
            fail(f"{slug}: fingerprint {meta.get('fingerprint')} != baseline {fp}")
        if not meta.get("source-url", "").startswith("http"):
            fail(f"{slug}: source-url not http")
    ok("website folders: files present, JSON valid, slug + fingerprint match")


# ------------------------------------------------------------ retrieval

def validate_retrieval(site_slugs: set[str]) -> None:
    for fname in ("industry-index.json", "style-index.json",
                  "component-index.json", "knowledge-map.json"):
        path = RETRIEVAL_DIR / fname
        if not path.exists():
            fail(f"retrieval: missing {fname}")
            continue
        try:
            data = json.loads(path.read_text(encoding="utf-8"))
        except Exception as exc:  # noqa: BLE001
            fail(f"retrieval: {fname} invalid JSON ({exc})")
            continue
        # index site slugs found anywhere in the file
        found = set(re.findall(r'"slug"\s*:\s*"([^"]+)"', path.read_text(encoding="utf-8")))
        unknown = found - site_slugs
        if unknown:
            fail(f"retrieval: {fname} references unknown slug(s): {sorted(unknown)}")
    check(True, "retrieval JSONs valid + reference known slugs")


# ---------------------------------------------------------- collections

def validate_collections(site_slugs: set[str]) -> None:
    for coll in sorted((REPO_ROOT / "references" / "collections").glob("*.md")):
        text = coll.read_text(encoding="utf-8")
        for m in re.finditer(r"\| `([a-z0-9-]+)` \|", text):
            slug = m.group(1)
            if slug not in site_slugs:
                fail(f"collection {coll.stem}: references unknown slug '{slug}'")
    ok("collections reference known website slugs")


# ------------------------------------------------- processes + copywriting

PROCESSES_REQUIRED = ["ui-build-playbook.md", "process-changelog.md",
                      "extraction-prompt.md"]


def validate_processes() -> None:
    procs = REPO_ROOT / "references" / "processes"
    if not procs.is_dir():
        fail("processes: references/processes/ missing")
        return
    for fname in PROCESSES_REQUIRED:
        path = procs / fname
        if not path.exists():
            fail(f"processes: missing {fname}")
            continue
        if not path.read_text(encoding="utf-8").strip():
            fail(f"processes: {fname} is empty")
    playbook = procs / "ui-build-playbook.md"
    changelog = procs / "process-changelog.md"
    if playbook.exists() and changelog.exists():
        text = playbook.read_text(encoding="utf-8")
        m = re.search(r"version:\s*(\d+\.\d+\.\d+)", text)
        if not m:
            fail("processes: playbook has no version: X.Y.Z header")
        elif "evidence" not in text.lower():
            fail("processes: playbook mentions no evidence")
        elif m.group(1) not in changelog.read_text(encoding="utf-8"):
            fail(f"processes: changelog has no entry for playbook v{m.group(1)}")
    for obs in sorted(procs.glob("*.md")):
        if obs.name in PROCESSES_REQUIRED:
            continue
        text = obs.read_text(encoding="utf-8").lower()
        if "status" not in text or "grade" not in text:
            fail(f"processes: observation {obs.name} lacks status/grading block")
    copy_file = REPO_ROOT / "references" / "copywriting" / "human-copy.md"
    if not copy_file.exists():
        fail("copywriting: references/copywriting/human-copy.md missing")
    else:
        text = copy_file.read_text(encoding="utf-8")
        if "## " not in text:
            fail("copywriting: human-copy.md has no sections")
        if "http" not in text:
            fail("copywriting: human-copy.md cites no sources")
    try:
        km = json.loads((RETRIEVAL_DIR / "knowledge-map.json").read_text(encoding="utf-8"))
    except Exception as exc:  # noqa: BLE001
        fail(f"processes: knowledge-map.json unreadable ({exc})")
        return
    if "ui build process" not in km.get("map", {}):
        fail("processes: knowledge-map.json has no 'ui build process' entry")
    ok("processes + copywriting: files present, version + changelog + map wired")


# ---------------------------------------------------------------- INDEX

def validate_index(site_slugs: set[str]) -> None:
    idx = (REPO_ROOT / "INDEX.md")
    if not idx.exists():
        fail("INDEX.md missing")
        return
    text = idx.read_text(encoding="utf-8")
    start = text.find("## Websites")
    if start == -1:
        fail("INDEX.md: Websites section not found")
        return
    chunk = text[start:]
    end = chunk.find("\n## ")
    if end != -1:
        chunk = chunk[:end]
    indexed = set()
    for line in chunk.splitlines():
        m = re.match(r"^\|\s*([a-z0-9-]+)\s*\|", line)
        if m and not set(m.group(1)) == {"-"}:
            indexed.add(m.group(1))
    if indexed != site_slugs:
        fail(f"INDEX.md Websites table mismatch: missing={site_slugs - indexed} "
             f"stale={indexed - site_slugs}")
    else:
        ok("INDEX.md Websites table matches website folders")


def main() -> None:
    print("validate: design-skills repository")
    validate_skill_md()
    validate_md_links()
    validate_websites()
    validate_processes()

    site_slugs = {d.name for d in WEBSITES_DIR.iterdir()
                  if d.is_dir() and not d.name.startswith("_")}
    validate_retrieval(site_slugs)
    validate_collections(site_slugs)
    validate_index(site_slugs)

    print("")
    if FAILURES:
        print(f"FAILED ({len(FAILURES)} issue(s)):")
        for f in FAILURES:
            print(f"  - {f}")
        sys.exit(1)
    print("PASS — repository is consistent")


if __name__ == "__main__":
    main()
