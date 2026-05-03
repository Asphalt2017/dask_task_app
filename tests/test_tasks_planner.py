"""Tests for tasks planner markdown discovery."""

from __future__ import annotations

from dask_task_app.pages.tasks_planner import TasksPlannerPage
from dask_task_app.utils.base_setting import TasksPlannerSettings


def test_discover_task_markdowns_reads_fixture_files() -> None:
    """Discover markdown files from the fixture directory."""
    page = TasksPlannerPage(TasksPlannerSettings(markdown_dir="tests/data/tasks"))
    tabs = page.discover_task_markdowns("tests/data/tasks")

    values = [tab["value"] for tab in tabs]
    assert "kitchen" in values
    assert "shopping" in values
