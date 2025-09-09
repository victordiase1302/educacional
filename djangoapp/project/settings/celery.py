from decouple import config

CELERY_BROKER_URL = config("REDIS_HOST")

CELERY_RESULT_BACKEND = config("REDIS_HOST")
