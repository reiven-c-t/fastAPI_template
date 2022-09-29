FROM --platform=linux/x86_64 python:3.10.7-bullseye
WORKDIR /app

COPY poetry.lock pyproject.toml ./
RUN pip install poetry && \
    poetry config virtualenvs.create false \
    && poetry install --only main

COPY server /app