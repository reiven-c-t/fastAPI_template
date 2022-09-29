FROM --platform=linux/x86_64 python:3.10.7-bullseye
WORKDIR /app

COPY pyproject.toml ./
RUN pip install poetry && \
    poetry config virtualenvs.create false \
    && poetry install --only main
