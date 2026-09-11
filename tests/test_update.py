"""Tests for scripts/update.py finalize snapshot-cleanup gating."""
import json
import sys

import update


def _site(sites_dir):
    folder = sites_dir / "acme"
    folder.mkdir(parents=True)
    (folder / "metadata.json").write_text(
        json.dumps(
            {"slug": "acme", "name": "Acme", "source-url": "https://acme.test"}
        ),
        encoding="utf-8",
    )
    (folder / "baseline.json").write_bytes(b'{"old": true}')
    return folder


def test_update_finalize_cleans_snapshot_on_success(tmp_path, monkeypatch) -> None:
    _site(tmp_path / "websites")
    monkeypatch.setattr(update, "WEBSITES_DIR", tmp_path / "websites")
    monkeypatch.setattr(update, "run_script", lambda name: 0)
    cleaned = []
    monkeypatch.setattr(
        update, "cleanup_consumed_snapshot", lambda p: cleaned.append(str(p)) or True
    )
    snap = tmp_path / "new_v0.28.0.json"
    snap.write_bytes(b'{"new": true}')
    monkeypatch.setattr(sys, "argv", ["update.py", "acme", "--finalize", str(snap)])
    update.main()
    assert cleaned == [str(snap)]
    assert (tmp_path / "websites" / "acme" / "baseline.json").read_bytes() == (
        b'{"new": true}'
    )


def test_update_finalize_keeps_snapshot_on_failure(tmp_path, monkeypatch) -> None:
    _site(tmp_path / "websites")
    monkeypatch.setattr(update, "WEBSITES_DIR", tmp_path / "websites")
    monkeypatch.setattr(
        update, "run_script", lambda name: 1 if name == "validate.py" else 0
    )
    cleaned = []
    monkeypatch.setattr(
        update, "cleanup_consumed_snapshot", lambda p: cleaned.append(str(p)) or True
    )
    snap = tmp_path / "new_v0.28.0.json"
    snap.write_bytes(b'{"new": true}')
    monkeypatch.setattr(sys, "argv", ["update.py", "acme", "--finalize", str(snap)])
    update.main()
    assert cleaned == []
    assert snap.exists()
