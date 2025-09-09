from django.db import models
from site_setup.utils.model_validators import validade_image
from videos.utils.embed_youtube import embed_video_youtube

# from django.urls import reverse


class Video(models.Model):
    class Platforms(models.TextChoices):
        YT = "YT", "YouTube"
        RM = "RM", "Rumble"
        EX = "EX", "Externo"

    site_setup = models.ForeignKey(
        'site_setup.SiteSetup',
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        verbose_name='Site ativo'
    )
    title = models.CharField(
        max_length=100, verbose_name='Título'
    )
    thumbnail = models.ImageField(
        upload_to='images/platforms/',
        blank=True,
        null=True,
        verbose_name='Thumbnail',
        validators=[validade_image]
    )
    link = models.URLField(
        null=True,
        blank=True,
    )
    streaming = models.CharField(
        max_length=2,
        choices=Platforms.choices,
        null=True,
        blank=True,
    )
    icons = models.ForeignKey(
        'platforms.StatusPlatform',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name='Icone'
    )
    order = models.PositiveSmallIntegerField(default=0, verbose_name='Posição')
    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name='Criado em'
    )
    updated_at = models.DateTimeField(
        auto_now=True, verbose_name='Atualizado em'
    )
    is_active = models.BooleanField(
        default=True, verbose_name='Video ativo'
    )

    def save(self, *args, **kwargs):
        if self.streaming == "YT":
            self.link = embed_video_youtube(self.link)
        super(Video, self).save(*args, **kwargs)

    @property
    def get_streaming_url(self):
        if self.link:
            return self.link

    def __str__(self):
        return self.title

    class Meta:
        ordering = ("order", "-updated_at")
        verbose_name = 'Video | Cadastro'
        verbose_name_plural = 'Videos | Cadastros'
