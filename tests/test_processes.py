"""Tests for the processes/ + copywriting/ content type and its wiring."""
import json
import re
from pathlib import Path

import pytest

import rebuild
import validate

REPO_ROOT = Path(__file__).resolve().parent.parent


@pytest.fixture()
def _reset_failures():
    validate.FAILURES = []
    yield
    validate.FAILURES = []


def test_index_builder_lists_processes_and_copywriting() -> None:
    md = rebuild.build_index_md([])
    assert "## Processes" in md
    assert "## Copywriting" in md
    assert "references/processes/ui-build-playbook.md" in md
    assert "references/copywriting/human-copy.md" in md


def test_real_repo_processes_pass(_reset_failures) -> None:
    validate.validate_processes()
    assert validate.FAILURES == []


def test_playbook_version_matches_changelog() -> None:
    procs = REPO_ROOT / "references" / "processes"
    text = (procs / "ui-build-playbook.md").read_text(encoding="utf-8")
    m = re.search(r"version:\s*(\d+\.\d+\.\d+)", text)
    assert m, "playbook needs a version: X.Y.Z header"
    log = (procs / "process-changelog.md").read_text(encoding="utf-8")
    assert m.group(1) in log


def test_knowledge_map_wires_process_and_copy() -> None:
    km = json.loads(
        (REPO_ROOT / "references" / "retrieval" / "knowledge-map.json").read_text(
            encoding="utf-8"
        )
    )
    assert "ui build process" in km["map"]
    assert "human copy / de-ai writing" in km["map"]
    for key in ("ui build process", "human copy / de-ai writing"):
        for f in km["map"][key]["files"]:
            assert (REPO_ROOT / f).exists(), f"mapped file missing: {f}"


def test_observation_templates_have_grading_block() -> None:
    procs = REPO_ROOT / "references" / "processes"
    obs = [p for p in procs.glob("*.md")
           if p.name not in validate.PROCESSES_REQUIRED]
    assert obs, "expected observation templates (claude-v1, astra-v1)"
    for path in obs:
        text = path.read_text(encoding="utf-8").lower()
        assert "status" in text and "grade" in text, path.name
