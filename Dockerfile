FROM --platform=linux/x86_64 python:3.10.7-bullseye as package_container

RUN mkdir /app
COPY ./pyproject.toml /app/
WORKDIR /app
RUN pip install poetry && \
    poetry config virtualenvs.create false && \
    poetry install --only main

FROM package_container
WORKDIR /app
CMD ["/bin/bash", "bin/run_server.sh"]