"""Dash app entrypoint."""

from __future__ import annotations

from dash import Dash, html

from dask_task_app.pages.tasks_planner import TasksPlannerPage
from dask_task_app.settings import AppSettings
from dask_task_app.utils.base_setting import TasksPlannerSettings


def build_app(settings: AppSettings) -> Dash:
    """Build and return the Dash app instance."""
    app = Dash(__name__)
    pages = _build_pages(settings)

    for page in pages:
        page.register_callbacks(app)

    app.layout = html.Div([page.build_layout() for page in pages])
    return app


def _build_pages(settings: AppSettings) -> list[TasksPlannerPage]:
    """Create page objects from typed page settings."""
    pages: list[TasksPlannerPage] = []
    for page_settings in settings.pages:
        if isinstance(page_settings, TasksPlannerSettings):
            pages.append(TasksPlannerPage(page_settings))
    return pages
