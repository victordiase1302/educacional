from django.db import models
from site_setup.utils.model_validators import validade_image


class Icon(models.Model):
    title = models.CharField(max_length=100, verbose_name='Nome')
    icon = models.ImageField(
        upload_to='images/icons/',
        blank=True,
        default='',
        validators=[validade_image],
        verbose_name='Icone'
    )
    order = models.PositiveSmallIntegerField(default=0, verbose_name='Ordem')
    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name='Criado em'
    )
    updated_at = models.DateTimeField(
        auto_now=True, verbose_name='Atualizado em'
    )
    is_filter = models.BooleanField(default=True, verbose_name='Será filtrado')
    is_active = models.BooleanField(default=True, verbose_name='Está ativo')

    def __str__(self):
        return str(self.title)

    class Meta:
        verbose_name = 'Plataforma | Icone da plataforma'
        verbose_name_plural = 'Plataformas | Icones da plataforma'
