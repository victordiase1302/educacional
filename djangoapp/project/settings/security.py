AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator", # noqa
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator", # noqa
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator", # noqa
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator", # noqa
    },
]

AUTH_USER_MODEL = "users.User"

CSRF_TRUSTED_ORIGINS = [
    'https://danielfortune.com.br',
    'https://desenvolvimento.danielfortune.com.br',
]

USE_X_FORWARDED_HOST = True
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
