#!/bin/sh
exec venv/bin/gunicorn -b :5100 --access-logfile - --error-logfile - bulletin:app