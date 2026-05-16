FROM python:3.14.0-slim AS runtime

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    DASK_TASK_APP_HOST=0.0.0.0 \
    DASK_TASK_APP_PORT=8050

WORKDIR /app

RUN addgroup --system app && adduser --system --ingroup app app

COPY pyproject.toml README.md ./
COPY dask_task_app ./dask_task_app

RUN pip install --no-cache-dir --upgrade pip \
    && pip install --no-cache-dir .

USER app

EXPOSE 8050

CMD ["python", "-m", "dask_task_app.main"]
