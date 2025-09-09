#!/bin/bash
set -e

python manage.py collectstatic --no-input

python manage.py makemigrations --no-input

python manage.py migrate --no-input

# python manage.py runserver 0.0.0.0:8000
gunicorn --config gunicorn-cfg.py project.wsgi