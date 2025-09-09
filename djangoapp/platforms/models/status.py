from django.db import models
from site_setup.utils.model_validators import validade_image

from os.path import splitext

def unique_file_path(instance, filename):
    base_filename, file_extension = splitext(filename)
    base_name = instance.name.lower()    
    new_filename = f"{base_name}{file_extension}"        
    return f'images/icons/{new_filename}'


class StatusPlatform(models.Model):
    name = models.CharField(max_length=100, verbose_name='Nome',)
    icon = models.ImageField(
        upload_to=unique_file_path,
        blank=True,
        null=True,
        validators=[validade_image],
        verbose_name='Icone'
    )
    cor_hex = models.CharField(
        max_length=7,
        verbose_name='Cor de fundo',
        help_text='Preencher de forma hexadecimal #000000',
        default='#000000'
    )
    order = models.PositiveSmallIntegerField(default=0, verbose_name='Ordem',)
    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name='Criado em'
    )
    updated_at = models.DateTimeField(
        auto_now=True, verbose_name='Atualizado em'
    )
    is_filter = models.BooleanField(default=True, verbose_name='Será filtrado')
    is_active = models.BooleanField(default=True, verbose_name='Está ativo')

    # def has_platform(self):
    #     return bool(self.cardtargetplatform_set.filter(is_active=True))

    def __str__(self):
        return str(self.name)

    class Meta:
        ordering = ("order", "-updated_at")
        verbose_name = 'Plataforma | Status'
        verbose_name_plural = 'Plataformas | Status'
