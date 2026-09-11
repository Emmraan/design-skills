"""Tests for scripts/validate.py repository checks."""
import json

import pytest

import validate


@pytest.fixture()
def _reset_failures():
    validate.FAILURES = []
    yield
    validate.FAILURES = []


def _write_fixture_repo(root) -> None:
    site = root / "references" / "websites" / "foo"
    site.mkdir(parents=True)
    (site / "metadata.json").write_text(
        json.dumps({"slug": "bar", "name": "Foo"}), encoding="utf-8"
    )
    (site / "analysis.md").write_text("# Foo analysis\n", encoding="utf-8")


def test_fixture_repo_fails_validation(tmp_path, monkeypatch, _reset_failures) -> None:
    _write_fixture_repo(tmp_path)
    monkeypatch.setattr(validate, "REPO_ROOT", tmp_path)
    monkeypatch.setattr(validate, "WEBSITES_DIR", tmp_path / "references" / "websites")
    monkeypatch.setattr(
        validate, "RETRIEVAL_DIR", tmp_path / "references" / "retrieval"
    )
    with pytest.raises(SystemExit) as exc:
        validate.main()
    assert exc.value.code == 1
    assert validate.FAILURES, "expected validation failures for the fixture repo"
    flat = "\n".join(validate.FAILURES)
    assert "SKILL.md missing" in flat
    assert "metadata.slug 'bar' != folder name" in flat
    assert "metadata missing field" in flat
    assert "baseline.json missing" in flat
    assert "retrieval: missing industry-index.json" in flat
    assert "INDEX.md missing" in flat


def test_real_repo_passes_validation(_reset_failures) -> None:
    validate.main()
    assert validate.FAILURES == []
