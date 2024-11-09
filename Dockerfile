FROM python:3.11-slim AS build

RUN pip install poetry==1.4.2
ENV POETRY_NO_INTERACTION=1 \
    POETRY_VIRTUALENVS_IN_PROJECT=1 \
    POETRY_VIRTUALENVS_CREATE=1 \
    POETRY_CACHE_DIR=/tmp/poetry_cache

WORKDIR /app
COPY pyproject.toml poetry.lock ./
RUN poetry install \
        --without dev \
        --no-root \
        --no-interaction \
    && rm -rf $POETRY_CACHE_DIR


FROM python:3.11-slim

ENV VIRTUAL_ENV=/app/.venv \
    PATH="/app/.venv/bin:$PATH"

COPY --from=build ${VIRTUAL_ENV} ${VIRTUAL_ENV}

COPY app ./app

ENTRYPOINT ["python", "-m", "app.app"]
