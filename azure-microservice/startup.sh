#!/bin/bash
exec gunicorn -k uvicorn.workers.UvicornWorker app:app --bind 0.0.0.0:8000
