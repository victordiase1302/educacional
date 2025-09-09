from django.apps import AppConfig


class CountersConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'counters'
    verbose_name = 'Contador'
    verbose_name_plural = 'Contadores'
