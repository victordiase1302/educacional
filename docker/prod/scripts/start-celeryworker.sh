#!/bin/bash

set -o errexit

set -o nounset

celery -A project worker --beat --scheduler django -l info
# celery -A project beat -l INFO --scheduler django_celery_beat.schedulers:DatabaseScheduler
