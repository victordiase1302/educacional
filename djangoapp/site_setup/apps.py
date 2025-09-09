from django.apps import AppConfig


class SiteSetupConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'site_setup'
    verbose_name = 'Configuração'
    verbose_name_plural = 'Configurações'
