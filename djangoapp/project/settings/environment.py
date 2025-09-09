from pathlib import Path

from decouple import config

BASE_DIR = Path(__file__).resolve().parent.parent.parent

DATA_DIR = BASE_DIR.parent / 'data' / 'web'

SECRET_KEY = config("SECRET_KEY")

DEBUG = config("DEBUG", default=False, cast=bool)

ALLOWED_HOSTS = config("ALLOWED_HOSTS").split(" ")

ROOT_URLCONF = "project.urls"

WSGI_APPLICATION = "project.wsgi.application"

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

X_FRAME_OPTIONS = 'SAMEORIGIN'

SITE_ID = 1

TELEGRAM_BOT_TOKEN = config("TELEGRAM")
TELEGRAM_SOFIA_SUPORTE = config("TELEGRAM_SOFIA_SUPORTE")
