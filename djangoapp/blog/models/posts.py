from django.db import models
from autoslug import AutoSlugField
from django.urls import reverse
from site_setup.utils.model_validators import validade_image


class Posts(models.Model):
    site_setup = models.ForeignKey(
        'site_setup.SiteSetup',
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        verbose_name='Site ativo'
    )
    title = models.CharField(max_length=255, verbose_name='Título do post')
    sub_title = models.CharField(
        max_length=255, 
        verbose_name='Subtítulo do post', 
        blank=True, 
        null=True,
    )
    slug = AutoSlugField(populate_from='title', unique=True)
    thumbnail = models.ImageField(
        upload_to='images/thumbnail/',
        blank=True,
        default='',
        validators=[validade_image]
    )
    post = models.TextField(blank=True, null=True, verbose_name='Post')
    order = models.PositiveSmallIntegerField(default=0, verbose_name='Posição')
    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name='Criado em'
    )
    updated_at = models.DateTimeField(
        auto_now=True, verbose_name='Atualizado em'
    )
    is_active = models.BooleanField(
        default=True, verbose_name='Post ativo'
    )

    @property
    def get_detail_url(self):
        return reverse("blog:post", kwargs={"slug": self.slug})

    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ("order", "-updated_at")
        verbose_name = 'Blog | Cadastro'
        verbose_name_plural = 'Blogs | Cadastros'
