"""CLI entrypoint module."""

from __future__ import annotations

from dask_task_app.app import build_app
from dask_task_app.utils.cli import load_runtime_settings


def main() -> None:
    """Run the Dash app with runtime settings."""
    settings = load_runtime_settings()
    app = build_app(settings)
    app.run(host=settings.host, port=settings.port, debug=settings.debug)


if __name__ == "__main__":
    main()
