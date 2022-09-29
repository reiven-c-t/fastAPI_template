#!/usr/bin bash

SCRIPT_DIR=$(cd $(dirname $0); pwd)
PROJECT_TOP=$(cd ${SCRIPT_DIR}/..; pwd)

poetry run python server/initialize_data.py

# docker exec fast_api_server sh /app/bin/init_db.sh