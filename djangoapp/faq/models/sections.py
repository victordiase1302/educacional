from django.db import models


class Section(models.Model):
    title = models.CharField(
        max_length=100,
        verbose_name='Título',
        blank=True,
        null=True,
    )
    sub_title = models.CharField(
        max_length=255,
        verbose_name='Subtítulo',
        blank=True,
        null=True,
    )
    order = models.PositiveSmallIntegerField(default=0, verbose_name='Posição')
    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name='Criado em'
    )
    updated_at = models.DateTimeField(
        auto_now=True, verbose_name='Atualizado em'
    )
    is_active = models.BooleanField(
        default=True, verbose_name='FAQ ativa'
    )

    @property
    def get_faqs(self):
        return self.faq_set.filter(is_active=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ("order", "-updated_at")
        verbose_name = 'FAQ | Seção'
        verbose_name_plural = 'FAQ | Seções'
