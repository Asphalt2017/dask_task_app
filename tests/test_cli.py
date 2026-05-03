"""Tests for CLI override behavior."""

from __future__ import annotations

import sys

from dask_task_app.utils.cli import load_runtime_settings


def test_cli_overrides_port_and_debug(monkeypatch) -> None:
    """Apply port and debug values from CLI."""
    monkeypatch.setattr(sys, "argv", ["app", "--port", "9999", "--debug"])

    settings = load_runtime_settings()
    assert settings.port == 9999
    assert settings.debug is True
