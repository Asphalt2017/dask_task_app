# Project: Dash Task App

## 2026-05-03 ---------------------------------

## Stage 1 Goal
Render task markdown files as dynamic tabs in the UI.

Example input files:
- `kitchen.md`
- `shopping.md`

Expected behavior:
- Each markdown file becomes one tab.
- Adding/removing markdown files updates available tabs.

## Requirements
1. App runs in terminal and is Docker-ready.
2. GitHub automation pipeline planned (deferred from Task 1 implementation).
3. Git-versioned, incremental delivery.

## Agreed Implementation Decisions (from chat)
- Use package import style:
  - `from dask_task_app.settings import AppSettings`
  - Avoid `src.settings` imports and any `src.*` package paths.
- Use abstract page architecture:
  - `base_page.py` defines `BasePage`.
  - `base_setting.py` defines `BasePageSettings`.
- Use Pydantic discriminator on page settings:
  - `category` distinguishes page setting models.
- Keep validators minimal:
  - Add validators only when needed (post-load normalization, file-read safety).
  - Path normalization belongs in `BasePageSettings` (not in `AppSettings`).
- Keep code minimal while preserving separation of concerns.
- Follow PEP8 with docstrings/type hints on public classes/methods.
- Enforce quality via `ruff` + `pre-commit`.
- Add `.gitignore` and `.dockerignore`.
- Python target: venv with Python 3.14 when environment supports it.

## Project Structure (target)
Use `app/` layout for all app code (no `src/` folder):

- `app/dask_task_app/`
  - `__init__.py`
  - `app.py`
  - `main.py`
  - `settings.py`
  - `base_page.py`
  - `base_setting.py`
  - `utils/`
    - `cli.py` (`--settings`, `--port`, `--debug`)
  - `pages/`
    - `tasks_planner.py`
  - `components/`
  - `templates/`
  - `assets/`
- `tests/data/tasks/` for markdown fixtures and early pytest compatibility.

## Settings Model
- `AppSettings` contains app-level runtime config (`host`, `port`, `debug`, `pages`).
- `pages` is a discriminated union keyed by `category`.
- First concrete page setting:
  - `TasksPlannerSettings(category="tasks_planner", markdown_dir=...)`.

## Task 1 Scope
Create scaffold + stubs:
- package structure,
- abstract contracts,
- typed settings + CLI override flow,
- initial tasks planner page with markdown discovery,
- tests for discriminator/CLI/discovery,
- lint/pre-commit setup.

Deferred:
- full real-time file watching,
- CI/CD workflow implementation,
- Docker runtime finalization.
