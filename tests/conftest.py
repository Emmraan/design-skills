"""Pytest bootstrap: make scripts/ importable.

The maintenance scripts use absolute imports (`from _common import ...`),
so the scripts directory must be on sys.path for the test suite.
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "scripts"))
