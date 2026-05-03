"""Tests for settings loading and discriminator behavior."""

from __future__ import annotations

import json

import pytest
from pydantic import ValidationError

from dask_task_app.settings import AppSettings, load_settings
from dask_task_app.utils.base_setting import TasksPlannerSettings


def test_discriminator_parses_tasks_planner_settings() -> None:
    """Parse page settings by category discriminator."""
    settings = AppSettings.model_validate(
        {
            "pages": [
                {
                    "category": "tasks_planner",
                    "markdown_dir": "tests/data/tasks",
                },
            ],
        },
    )
    assert isinstance(settings.pages[0], TasksPlannerSettings)


def test_unknown_category_raises_validation_error() -> None:
    """Raise validation error when category is unknown."""
    with pytest.raises(ValidationError):
        AppSettings.model_validate({"pages": [{"category": "unknown"}]})


def test_load_settings_from_file(tmp_path) -> None:
    """Load settings from JSON file."""
    config_file = tmp_path / "settings.json"
    config_file.write_text(json.dumps({"port": 9000}), encoding="utf-8")

    settings = load_settings(str(config_file))
    assert settings.port == 9000
