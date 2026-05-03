"""Tasks planner page implementation."""

from __future__ import annotations

from pathlib import Path
from typing import Any

from dash import Dash, dcc, html

from dask_task_app.utils.base_page import BasePage
from dask_task_app.utils.base_setting import TasksPlannerSettings


class TasksPlannerPage(BasePage):
    """Render markdown tasks as tabbed content."""

    settings: TasksPlannerSettings

    def __init__(self, settings: TasksPlannerSettings) -> None:
        """Initialize page with typed settings."""
        super().__init__(settings)

    def build_layout(self) -> Any:
        """Build page layout with one tab per markdown file."""
        tabs = self.discover_task_markdowns(self.settings.markdown_dir)
        if not tabs:
            return html.Div("No markdown task files found.")

        return dcc.Tabs(
            id="task-tabs",
            value=tabs[0]["value"],
            children=[
                dcc.Tab(
                    label=tab["label"],
                    value=tab["value"],
                    children=dcc.Markdown(tab["content"]),
                )
                for tab in tabs
            ],
        )

    def register_callbacks(self, app: Dash) -> None:
        """Register callbacks for the page."""
        _ = app

    def discover_task_markdowns(self, content_dir: str) -> list[dict[str, str]]:
        """Read markdown files and convert them into tab payloads."""
        tabs: list[dict[str, str]] = []
        for file_path in sorted(Path(content_dir).glob("*.md")):
            content = self._safe_read_file(file_path)
            if content is None:
                continue
            tabs.append(
                {
                    "label": file_path.stem.replace("_", " ").title(),
                    "value": file_path.stem,
                    "content": content,
                },
            )
        return tabs

    def _safe_read_file(self, file_path: Path) -> str | None:
        """Read UTF-8 markdown file and skip unreadable files."""
        try:
            return file_path.read_text(encoding="utf-8")
        except (OSError, UnicodeDecodeError):
            return None
