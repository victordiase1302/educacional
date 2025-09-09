from decouple import config

from .environment import BASE_DIR, DATA_DIR

STATIC_URL = "/static/"
STATIC_ROOT = DATA_DIR / 'static'
STATICFILES_DIRS = [BASE_DIR / 'static']

MEDIA_URL = "/media/"
MEDIA_ROOT = DATA_DIR / 'media'

STORAGES = {
    "default": {
        "BACKEND": "storages.backends.s3boto3.S3Boto3Storage",
    },
    "staticfiles": {
        "BACKEND": "django.contrib.staticfiles.storage.StaticFilesStorage",
    },
}
# "storages.backends.s3boto3.S3Boto3Storage",

AWS_ACCESS_KEY_ID = config("AWS_S3_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY = config("AWS_S3_SECRET_ACCESS_KEY")
AWS_STORAGE_BUCKET_NAME = config("AWS_S3_BUCKET_NAME")
AWS_REGION_NAME = config("AWS_REGION_NAME")
AWS_QUERYSTRING_EXPIRE = 5
AWS_S3_CUSTOM_DOMAIN = 'dzdzhg4kdrerf.cloudfront.net'
# STATICFILES_STORAGE = "storages.backends.s3boto3.S3Boto3Storage"
AWS_S3_OBJECT_PARAMETERS = {
    'CacheControl': 'max-age=0, no-cache, no-store, must-revalidate',
}

DOMAIN = config('DOMAIN')

SUB_DEV = config("SUB_DEV").split(" ")

PROD_ECR = config("PROD_ECR").split(" ")

PROD_IPROF = config("PROD_IPROF").split(" ")

ALLOWED_START = config('ALLOWED_START').split(" ")

DJANGO_ADMIN_URL = config("DJANGO_ADMIN_URL", default="admin/")
