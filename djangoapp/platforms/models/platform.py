from autoslug import AutoSlugField
from django.db import models
from django.urls import reverse
from site_setup.utils.model_validators import validade_image


from os.path import splitext

def unique_file_path(instance, filename):
    base_filename, file_extension = splitext(filename)
    base_name = instance.name.lower()    
    new_filename = f"{base_name}{file_extension}"        
    return f'images/platforms/{new_filename}'


class Platform(models.Model):
    site_setup = models.ForeignKey(
        'site_setup.SiteSetup',
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        verbose_name='Site ativo'
    )
    name = models.CharField(max_length=100, verbose_name='Nome da plataforma')
    family_name = models.CharField(
        max_length=100, verbose_name='Nome da família', null=True, blank=True
    )
    status = models.ForeignKey(
        'StatusPlatform',
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        verbose_name="Status"
    )
    slug = AutoSlugField(populate_from='name', unique=True)
    logo = models.ImageField(
        upload_to=unique_file_path,
        blank=True,
        default='',
        validators=[validade_image]
    )
    icons = models.ManyToManyField(
        'StatusPlatform',
        blank=True,
        verbose_name='Icones',
        related_name='icons'
    )
    min_deposit = models.CharField(
        max_length=50, verbose_name='Depósito mínimo', null=True, blank=True
    )
    min_cash = models.CharField(
        max_length=50, verbose_name='Saque mínimo', null=True, blank=True
    )
    bonus = models.CharField(max_length=50, null=True, blank=True)
    description = models.TextField(
        blank=True, null=True, verbose_name='Descrição'
    )
    specific_detail = models.ManyToManyField(
        'SpecificDetail', blank=True, verbose_name='Detalhes específicos'
    )
    name_link = models.CharField(
        max_length=25,
        default='Link do Daniel',
        verbose_name='Nome descritivo do link'
    )
    lucky_link = models.URLField(
        blank=True, null=True, verbose_name='Link'
    )
    is_payer = models.BooleanField(
        default=False, verbose_name='Favorita'
    )
    is_favorite = models.BooleanField(
        default=False, verbose_name='Destaque'
    )
    is_old = models.BooleanField(
        default=False, verbose_name='Panela velha'
    )
    order = models.PositiveSmallIntegerField(default=0, verbose_name='Posição')
    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name='Criado em'
    )
    updated_at = models.DateTimeField(
        auto_now=True, verbose_name='Atualizado em'
    )
    is_active = models.BooleanField(
        default=True, verbose_name='Plataforma ativa'
    )

    @property
    def get_detail_url(self):
        return reverse("platforms:platform", kwargs={"slug": self.slug})

    @property
    def get_format_as_timezone(self):
        return self.created_at.astimezone().strftime('%d/%m/%Y %H:%M')

    def __str__(self):
        return self.name

    class Meta:
        ordering = ("order", "-updated_at")
        verbose_name = 'Plataforma | Cadastro'
        verbose_name_plural = 'Plataformas | Cadastros'
