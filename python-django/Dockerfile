ARG PYTHON_VERSION=3.11
ARG POETRY_VERSION=1.4.2

FROM python:${PYTHON_VERSION}-slim as build-base

# deps
ENV DEPS_PSYCOPG2='python3-dev libpq-dev gcc'

SHELL ["/bin/bash", "-o", "pipefail", "-c"]
# hadolint ignore=DL3008
RUN apt-get update && \
    apt-get install --no-install-recommends -y curl ${DEPS_PSYCOPG2} && \
    apt-get purge -y --auto-remove -o APT:AutoRemove:RecommendsImportant=false && \
    rm -rf /var/lib/apt/lists/*

# poetry
# https://python-poetry.org/docs/configuration/#using-environment-variables
ENV POETRY_NO_INTERACTION=1 \
    POETRY_VIRTUALENVS_CREATE=false \
    POETRY_HOME=/opt/poetry \
    POETRY_VERSION=${POETRY_VERSION}

RUN curl -sSL https://install.python-poetry.org | python -

ENV PYTHONUNBUFFERED=1 \
    # paths
    VENV_PATH="/opt/pysetup/.venv" \
    PYSETUP_PATH="/opt/pysetup"

# prepend poetry and venv to path
ENV PATH="$POETRY_HOME/bin:$VENV_PATH/bin:$PATH"


FROM build-base as python-base

WORKDIR $PYSETUP_PATH

COPY poetry.lock pyproject.toml ./
RUN poetry install --no-root --no-cache

ENV APP_ROOT /app
WORKDIR ${APP_ROOT}

COPY . ${APP_ROOT}
