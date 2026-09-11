"""Tests for scripts/add.py finalize snapshot-cleanup gating."""
import json

import add


def test_finalize_cleans_snapshot_on_success(tmp_path, monkeypatch) -> None:
    monkeypatch.setattr(add, "WEBSITES_DIR", tmp_path / "websites")
    calls = []
    monkeypatch.setattr(add, "run_script", lambda name: calls.append(name) or 0)
    cleaned = []
    monkeypatch.setattr(
        add, "cleanup_consumed_snapshot", lambda p: cleaned.append(str(p)) or True
    )
    snap = tmp_path / "snap_v0.28.0.json"
    snap.write_bytes(b'{"tokens": true}')
    add.finalize("https://acme.test", "acme", str(snap), 5)
    assert calls == ["rebuild.py", "validate.py"]
    assert cleaned == [str(snap)]
    folder = tmp_path / "websites" / "acme"
    assert (folder / "baseline.json").read_bytes() == b'{"tokens": true}'
    meta = json.loads((folder / "metadata.json").read_text(encoding="utf-8"))
    assert meta["fingerprint"] != "pending"


def test_finalize_keeps_snapshot_on_failure(tmp_path, monkeypatch) -> None:
    monkeypatch.setattr(add, "WEBSITES_DIR", tmp_path / "websites")
    codes = {"rebuild.py": 0, "validate.py": 1}
    monkeypatch.setattr(add, "run_script", lambda name: codes[name])
    cleaned = []
    monkeypatch.setattr(
        add, "cleanup_consumed_snapshot", lambda p: cleaned.append(str(p)) or True
    )
    snap = tmp_path / "snap_v0.28.0.json"
    snap.write_bytes(b'{"tokens": true}')
    add.finalize("https://acme.test", "acme", str(snap), 5)
    assert cleaned == []
    assert snap.exists()
