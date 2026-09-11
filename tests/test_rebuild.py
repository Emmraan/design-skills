"""Tests for scripts/rebuild.py index builders."""
import pytest

from rebuild import (
    build_industry_index,
    build_style_index,
    classify_component,
    parse_component_map,
)

ANALYSIS_SAMPLE = """# Analysis

## 10. Component Map

1. Hero banner \u2014 full-viewport intro with a single CTA.
2. Pricing grid - three tiers, middle tier highlighted.
3. Footer

## 11. Pattern Position

Something else.

1. Should not appear \u2014 this is section 11.
"""


def test_parse_component_map_em_dash() -> None:
    items = parse_component_map(ANALYSIS_SAMPLE)
    assert items[0] == ("Hero banner", "full-viewport intro with a single CTA")


def test_parse_component_map_hyphen() -> None:
    items = parse_component_map(ANALYSIS_SAMPLE)
    assert items[1] == ("Pricing grid", "three tiers, middle tier highlighted")


def test_parse_component_map_no_separator() -> None:
    items = parse_component_map(ANALYSIS_SAMPLE)
    assert items[2] == ("Footer", "")


def test_parse_component_map_stops_at_section_11() -> None:
    items = parse_component_map(ANALYSIS_SAMPLE)
    assert len(items) == 3
    assert all("Should not appear" not in note for _, note in items)


def test_parse_component_map_missing_section() -> None:
    assert parse_component_map("# Analysis\n\nNo component map here.\n") == []


@pytest.mark.parametrize(
    ("label", "expected"),
    [
        ("Hero banner", "hero"),
        ("Top navigation bar", "navbar"),
        ("Pricing plans", "pricing"),
        ("Customer testimonials", "testimonials"),
        ("Mystery Widget Zone", None),
    ],
)
def test_classify_component(label: str, expected: str | None) -> None:
    assert classify_component(label) == expected


def _site(**overrides: str) -> dict:
    site = {
        "slug": "acme",
        "name": "Acme",
        "industry": "fintech",
        "style": "minimal",
        "theme": "light",
    }
    site.update(overrides)
    return site


def test_industry_index_preserves_curated_prose() -> None:
    prev = {
        "description": "custom description",
        "industries": {
            "fintech": {
                "pattern": "P",
                "collection": "C",
                "borrow": "B",
                "sites": [{"slug": "stale", "name": "Stale"}],
            }
        },
    }
    out = build_industry_index([_site()], prev)
    fintech = out["industries"]["fintech"]
    assert fintech["pattern"] == "P"
    assert fintech["collection"] == "C"
    assert fintech["borrow"] == "B"
    # structure is rebuilt from source of truth, not kept from prev
    assert fintech["sites"] == [
        {"slug": "acme", "name": "Acme", "style": "minimal", "theme": "light"}
    ]
    assert out["description"] == "custom description"


def test_industry_index_new_industry_has_no_curated_keys() -> None:
    out = build_industry_index([_site(industry="healthcare")], {})
    assert set(out["industries"]["healthcare"]) == {"sites"}
    assert "version" in out and out["version"] == "1.0.0"


def test_style_index_preserves_signature() -> None:
    prev = {"styles": {"minimal": {"signature": "S", "sites": []}}}
    out = build_style_index([_site()], prev)
    minimal = out["styles"]["minimal"]
    assert minimal["signature"] == "S"
    assert minimal["sites"] == [
        {"slug": "acme", "name": "Acme", "industry": "fintech", "theme": "light"}
    ]
