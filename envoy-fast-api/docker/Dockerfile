FROM python:3.11

ARG BUILD_PROD

ENV POETRY_HOME=/etc/poetry \
    POETRY_VERSION=1.2.0 \
    POETRY_VIRTUALENVS_CREATE=false \
    POETRY_NO_INTERACTION=1 \
    POETRY_OPTION=${BUILD_PROD:+"--no-dev"}

SHELL ["/bin/bash", "-l", "-c"]

WORKDIR /app

COPY app/poetry.lock app/pyproject.toml ./

RUN curl -sSL https://install.python-poetry.org | python - \
    && $POETRY_HOME/bin/poetry install $POETRY_OPTION --no-ansi \
    && rm -rf ~/.cache/pip \
    && rm -rf ~/.cache/pypoetry

CMD ["/usr/local/bin/uvicorn", "main:app", "--host", "0.0.0.0"]
