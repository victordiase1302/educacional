from django.db import models


class FAQ(models.Model):
    site_setup = models.ForeignKey(
        'site_setup.SiteSetup',
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        verbose_name='Site ativo'
    )
    section = models.ForeignKey(
        'Section',
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        verbose_name='Seção'
    )
    title = models.CharField(max_length=100, verbose_name='Título')
    icon_fontawesome = models.CharField(max_length=255, verbose_name='Icone')
    description = models.TextField(
        blank=True,
        null=True,
        verbose_name='Descrição',
        help_text='Para separar entre parágrafos use ; '
    )
    order = models.PositiveSmallIntegerField(default=0, verbose_name='Posição')
    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name='Criado em'
    )
    updated_at = models.DateTimeField(
        auto_now=True, verbose_name='Atualizado em'
    )
    in_main_page = models.BooleanField(
        default=True, verbose_name='Na página principal'
    )
    is_active = models.BooleanField(
        default=True, verbose_name='FAQ ativa'
    )

    def __str__(self):
        return self.title

    class Meta:
        ordering = ("order", "-updated_at")
        verbose_name = 'FAQ | Cadastro'
        verbose_name_plural = 'FAQ | Cadastros'
