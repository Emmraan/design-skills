"""Tests for scripts/_common.py shared helpers."""
import hashlib

import pytest

import _common
from _common import (
    DEMBRANDT_CRAWL,
    cleanup_consumed_snapshot,
    dembrandt_command,
    fingerprint,
    slugify,
)


@pytest.mark.parametrize(
    ("url", "expected"),
    [
        ("https://example.com/", "example"),
        ("https://example.com", "example"),
        ("https://www.example.com/pricing", "example"),
        ("https://WWW.Example.COM/", "example"),
        ("https://www.some-app.io/x", "some-app"),
        ("https://my-site.io", "my-site"),
        ("https://example.co.uk/", "example"),
        ("https://app.example.com/", "app"),
        ("http://localhost:3000/", "localhost"),
        ("https://example.com:8080/x", "example"),
        ("https://some_app.io/", "someapp"),
    ],
)
def test_slugify(url: str, expected: str) -> None:
    assert slugify(url) == expected


def test_fingerprint_is_sha1_hex12_upper(tmp_path) -> None:
    baseline = tmp_path / "baseline.json"
    baseline.write_bytes(b'{"a": 1}')
    expected = hashlib.sha1(b'{"a": 1}').hexdigest().upper()[:12]
    result = fingerprint(baseline)
    assert result == expected
    assert len(result) == 12
    assert result == result.upper()


def test_dembrandt_command_default_shape() -> None:
    cmd = dembrandt_command("https://example.com")
    assert cmd == (
        "npx dembrandt https://example.com "
        "--save-output --design-md --wcag "
        f"--crawl {DEMBRANDT_CRAWL}"
    )


def test_dembrandt_command_crawl_override() -> None:
    assert dembrandt_command("https://example.com", crawl=2).endswith("--crawl 2")


def test_dembrandt_command_compare_flag() -> None:
    cmd = dembrandt_command(
        "https://example.com", compare="references/websites/example/baseline.json"
    )
    assert "--compare references/websites/example/baseline.json" in cmd


def test_dembrandt_command_extra_flags() -> None:
    assert dembrandt_command("https://example.com", extra="--foo").endswith("--foo")


def _snapshot_tree(root):
    dom = root / "example.com"
    dom.mkdir(parents=True)
    snap = dom / "2026-01-01T00-00-00-000Z_v0.28.0.json"
    snap.write_bytes(b'{"ok": true}')
    (dom / "DESIGN.md").write_text("# design\n", encoding="utf-8")
    return dom, snap


def test_cleanup_removes_snapshot_and_emptied_folder(tmp_path, monkeypatch) -> None:
    monkeypatch.setattr(_common, "OUTPUT_DIR", tmp_path)
    dom, snap = _snapshot_tree(tmp_path)
    assert cleanup_consumed_snapshot(snap) is True
    assert not snap.exists()
    assert not dom.exists()


def test_cleanup_keeps_folder_with_remaining_snapshot(tmp_path, monkeypatch) -> None:
    monkeypatch.setattr(_common, "OUTPUT_DIR", tmp_path)
    dom, snap = _snapshot_tree(tmp_path)
    other = dom / "2026-02-02T00-00-00-000Z_v0.28.0.json"
    other.write_bytes(b'{"ok": true}')
    assert cleanup_consumed_snapshot(snap) is True
    assert not snap.exists()
    assert dom.exists()
    assert other.exists()


def test_cleanup_never_removes_output_dir_itself(tmp_path, monkeypatch) -> None:
    monkeypatch.setattr(_common, "OUTPUT_DIR", tmp_path)
    snap = tmp_path / "2026-01-01T00-00-00-000Z_v0.28.0.json"
    snap.write_bytes(b'{"ok": true}')
    assert cleanup_consumed_snapshot(str(snap)) is True
    assert not snap.exists()
    assert tmp_path.exists()


def test_cleanup_missing_file_is_noop(tmp_path, monkeypatch) -> None:
    monkeypatch.setattr(_common, "OUTPUT_DIR", tmp_path)
    assert cleanup_consumed_snapshot(tmp_path / "nope_v0.28.0.json") is False


def test_cleanup_refuses_paths_outside_output(tmp_path, monkeypatch) -> None:
    monkeypatch.setattr(_common, "OUTPUT_DIR", tmp_path / "output")
    outside = tmp_path / "elsewhere_v0.28.0.json"
    outside.write_bytes(b'{"ok": true}')
    assert cleanup_consumed_snapshot(outside) is False
    assert outside.exists()
