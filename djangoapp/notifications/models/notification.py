from django.db import models


class Notification(models.Model):
    class Colors(models.TextChoices):
        secondary = "secondary", "Azul"
        success = "success", "Verde"
        info = "info", "Azul Claro"
        warning = "warning", "Amarelo"
        danger = "danger", "Vermelho"
        dark = "dark", "Preto"
        light = "light", "Branco"

    class Emojis(models.TextChoices):
        smile = "smile", "😊"
        nice = "nice", "👍"
        checked = "checked", "✔"
        info = "info", "❕"
        warning = "warning", "⚠"
        danger = "danger", "🛑"

    site_setup = models.ForeignKey(
        "site_setup.SiteSetup",
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        verbose_name="Site ativo",
    )
    message = models.CharField(max_length=255, verbose_name="Mensagem")
    link = models.URLField(null=True, blank=True)
    color = models.CharField(
        max_length=20,
        verbose_name="Cor do aviso",
        choices=Colors.choices,
        default="info",
    )
    emoji = models.CharField(
        max_length=20,
        verbose_name="Emoji",
        choices=Emojis.choices,
        null=True,
        blank=True,
    )
    date_to_send = models.DateField(
        verbose_name='Data de envio',
        null=True,
        blank=True
    )
    time_to_send = models.TimeField(
        verbose_name='Hora do envio',
        null=True,
        blank=True
    )
    days_to_repeat = models.PositiveIntegerField(
        verbose_name='Quatidade de dias',
        null=True,
        default=0
    )
    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name="Criado em"
    )
    updated_at = models.DateTimeField(
        auto_now=True, verbose_name="Atualizado em"
    )
    is_active = models.BooleanField(
        default=True, verbose_name="Notificação ativa"
    )

    def __str__(self):
        return self.message

    class Meta:
        ordering = ("-updated_at",)
        verbose_name = "Notificação | Cadastro"
        verbose_name_plural = "Notificações | Cadastros"
