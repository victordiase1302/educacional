from django.apps import AppConfig


class PlatformsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'platforms'
    verbose_name = 'Plataforma'
    verbose_name_plural = 'Plataformas'

    def ready(self, *args, **kwargs):
        import platforms.signals  # noqa

        return super().ready(*args, **kwargs)
