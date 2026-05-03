"""Base settings models for pages."""

from __future__ import annotations

from pathlib import Path
from typing import Annotated, Literal

from pydantic import BaseModel, Field, model_validator


class BasePageSettings(BaseModel):
    """Base class for page-specific settings."""

    category: str

    @model_validator(mode="after")
    def normalize_paths(self) -> BasePageSettings:
        """Normalize path-like fields after model load."""
        markdown_dir = getattr(self, "markdown_dir", None)
        if markdown_dir:
            self.markdown_dir = str(Path(markdown_dir))
        return self


class TasksPlannerSettings(BasePageSettings):
    """Settings for the tasks planner page."""

    category: Literal["tasks_planner"] = "tasks_planner"
    markdown_dir: str = "tests/data/tasks"


PageSettingsUnion = Annotated[
    TasksPlannerSettings,
    Field(discriminator="category"),
]
