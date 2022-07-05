FROM python:3.9

ARG ARTIFACT_REPO

WORKDIR /app

ENV POETRY_HOME=/etc/poetry \
    POETRY_VERSION=1.1.13 \
    POETRY_VIRTUALENVS_CREATE=false \
    POETRY_NO_INTERACTION=1

COPY ./pyproject.toml ./poetry.lock ./

RUN curl -sSL https://install.python-poetry.org | python - \
    && $POETRY_HOME/bin/poetry config repositories.codeartifact $ARTIFACT_REPO
RUN --mount=type=secret,id=auth,required,dst=/root/.config/pypoetry/auth.toml \
    $POETRY_HOME/bin/poetry install --no-ansi
