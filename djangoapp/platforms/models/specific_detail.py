from django.db import models


class SpecificDetail(models.Model):
    title = models.CharField(max_length=255, verbose_name='Nome')
    order = models.PositiveSmallIntegerField(default=0, verbose_name='Ordem')
    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name='Criado em'
    )
    updated_at = models.DateTimeField(
        auto_now=True, verbose_name='Atualizado em'
    )
    is_active = models.BooleanField(default=True, verbose_name='Está ativo')

    def __str__(self):
        return str(self.title)

    class Meta:
        verbose_name = 'Plataforma | Detalhe especifico'
        verbose_name_plural = 'Plataformas | Detalhes especificos'
