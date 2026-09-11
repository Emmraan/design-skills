"""Tests for scripts/_common.py shared helpers."""
import hashlib

import pytest

from _common import DEMBRANDT_CRAWL, dembrandt_command, fingerprint, slugify


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
