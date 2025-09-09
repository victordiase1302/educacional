from django.apps import AppConfig


class NotificationsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'notifications'
    verbose_name = "Notificação"
    verbose_name_plural = "Notificações"


    def ready(self, *args, **kwargs) -> None:
        import notifications.signals  # noqa

        return super().ready(*args, **kwargs)
