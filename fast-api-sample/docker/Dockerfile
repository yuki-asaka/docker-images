FROM python:3.9

ARG BUILD_PROD

ENV POETRY_HOME=/etc/poetry \
    POETRY_VERSION=1.1.13 \
    POETRY_VIRTUALENVS_CREATE=false \
    POETRY_NO_INTERACTION=1 \
    POETRY_OPTION=${BUILD_PROD:+"--no-dev"}

SHELL ["/bin/bash", "-l", "-c"]

WORKDIR /app

COPY poetry.lock pyproject.toml ./

RUN curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python - \
    && source $POETRY_HOME/env \
    && poetry install $POETRY_OPTION --no-ansi \
    && rm -rf ~/.cache/pip \
    && rm -rf ~/.cache/pypoetry

#CMD ["/usr/local/bin/uvicorn", "main:app", "--host", "0.0.0.0"]
CMD ["/usr/local/bin/gunicorn", "main:app", \
    "--worker-class", "uvicorn.workers.UvicornWorker", \
    "--bind", "0.0.0.0:80"]
