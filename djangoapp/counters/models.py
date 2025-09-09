from django.db import models


class Visit(models.Model):
    ip_address = models.CharField(
        verbose_name='IP', max_length=100, null=True, blank=True
    )
    referer = models.CharField(
        verbose_name='Referencia',
        max_length=50,
        default='https://danielfortune.com.br/'
    )
    created_at = models.DateTimeField(auto_now_add=True)
    is_mobile = models.BooleanField(verbose_name='Celular', default=False)
    is_pwa = models.BooleanField(verbose_name='PWA', default=False)
    is_iphone = models.BooleanField(verbose_name='Iphone', default=False)

    @property
    def get_format_as_timezone(self):
        return self.created_at.astimezone().strftime('%d/%m/%Y %H:%M')

    def __str__(self):
        return str(self.id)

    class Meta:
        ordering = ("-created_at",)
        verbose_name = 'Contador de visita'
        verbose_name_plural = 'Contador de visitas'


class Services(models.Model):
    service = models.CharField(max_length=255)
    ip_address = models.CharField(
        verbose_name='IP', max_length=100, null=True, blank=True
    )
    is_mobile = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    @property
    def get_format_as_timezone(self):
        return self.created_at.astimezone().strftime('%d/%m/%Y %H:%M')

    def __str__(self):
        return str(self.service)

    class Meta:
        ordering = ("-created_at",)
        verbose_name = 'Contador de serviço'
        verbose_name_plural = 'Contador de serviços'
