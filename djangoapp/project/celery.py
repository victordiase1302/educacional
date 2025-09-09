from __future__ import absolute_import, unicode_literals

import os

from celery import Celery
from django.conf import settings

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project.settings")
# os.environ.setdefault('FORKED_BY_MULTIPROCESSING', '1')

app = Celery("project")
# app = Celery('energy', broker='amqp://localhost')

app.config_from_object("django.conf:settings", namespace="CELERY")

app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)
