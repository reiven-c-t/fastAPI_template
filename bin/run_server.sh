#!/usr/bin bash

SCRIPT_DIR=$(cd $(dirname $0); pwd)
PROJECT_TOP=$(cd ${SCRIPT_DIR}/..; pwd)
cd $PROJECT_TOP/

# Create initial data in DB
poetry run uvicorn main:app --reload --host 0.0.0.0 --port 8000 --app-dir server