"""Application settings and loading helpers."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

import yaml
from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict

from dask_task_app.utils.base_setting import PageSettingsUnion


class AppSettings(BaseSettings):
    """Top-level application settings."""

    model_config = SettingsConfigDict(env_prefix="DASK_TASK_APP_", extra="ignore")

    host: str = "127.0.0.1"
    port: int = 8050
    debug: bool = False
    pages: list[PageSettingsUnion] = Field(
        default_factory=lambda: [{"category": "tasks_planner"}],
    )


def load_settings(path: str | None = None) -> AppSettings:
    """Load settings from a file when provided, else from defaults/env."""
    if not path:
        return AppSettings()

    raw = _read_settings_file(path)
    return AppSettings.model_validate(raw)


def _read_settings_file(path: str) -> dict[str, Any]:
    """Read a JSON/YAML settings file from disk."""
    file_path = Path(path)
    with file_path.open("r", encoding="utf-8") as file:
        suffix = file_path.suffix.lower()
        if suffix == ".json":
            return json.load(file)
        if suffix in {".yaml", ".yml"}:
            data = yaml.safe_load(file)
            return data or {}
    raise ValueError(f"Unsupported settings file type: {file_path.suffix}")
