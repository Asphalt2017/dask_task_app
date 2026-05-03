"""Abstract page contract for Dash pages."""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Any

from dash import Dash

from dask_task_app.utils.base_setting import BasePageSettings


class BasePage(ABC):
    """Base interface for application pages."""

    def __init__(self, settings: BasePageSettings) -> None:
        """Store page settings."""
        self.settings = settings

    @abstractmethod
    def build_layout(self) -> Any:
        """Build and return the page layout."""

    @abstractmethod
    def register_callbacks(self, app: Dash) -> None:
        """Register callbacks for the page."""
