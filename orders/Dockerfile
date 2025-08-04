FROM python:slim

WORKDIR /app

ENV POETRY_NO_INTERACTION=1 \
    POETRY_VIRTUALENVS_IN_PROJECT=1 \
    POETRY_VIRTUALENVS_CREATE=1 \
    POETRY_CACHE_DIR=/tmp/poetry_cache

RUN pip install poetry

COPY . .

RUN poetry install

EXPOSE 8080

CMD ["poetry", "run", "gunicorn", "--bind", "0.0.0.0:8080", "--workers", "1", "main:app"]
