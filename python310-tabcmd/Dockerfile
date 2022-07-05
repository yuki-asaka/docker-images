FROM python:3.10-buster

ARG FUNCTION_DIR="/function"
ARG BUILD_PROD

ENV POETRY_HOME=/etc/poetry \
    POETRY_VERSION=1.1.13 \
    POETRY_VIRTUALENVS_CREATE=false \
    POETRY_NO_INTERACTION=1 \
    POETRY_OPTION=${BUILD_PROD:+"--no-dev"}

WORKDIR ${FUNCTION_DIR}
COPY pyproject.toml ${FUNCTION_DIR}/

RUN curl -sSL https://install.python-poetry.org | python3 - \
    && $POETRY_HOME/bin/poetry install ${POETRY_OPTION} --no-ansi
