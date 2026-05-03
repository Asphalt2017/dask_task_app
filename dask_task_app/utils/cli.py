"""CLI helpers for runtime configuration."""

from __future__ import annotations

import argparse

from dask_task_app.settings import AppSettings, load_settings


class CliOverrides(argparse.Namespace):
    """Typed namespace for CLI overrides."""

    settings: str | None
    port: int | None
    debug: bool | None


def parse_args() -> CliOverrides:
    """Parse command-line arguments."""
    parser = argparse.ArgumentParser(description="Run the Dash task planner app")
    parser.add_argument("--settings", type=str, default=None)
    parser.add_argument("--port", type=int, default=None)
    parser.add_argument("--debug", action="store_true")
    return parser.parse_args(namespace=CliOverrides())


def load_runtime_settings() -> AppSettings:
    """Load settings and apply CLI overrides."""
    args = parse_args()
    app_settings = load_settings(args.settings)

    if args.port is not None:
        app_settings.port = args.port
    if args.debug:
        app_settings.debug = True

    return app_settings
