from django.db import models
from site_setup.utils.images import resize_image
from site_setup.utils.model_validators import validade_image, validate_png


class SiteSetup(models.Model):
    title = models.CharField(max_length=65)
    description = models.CharField(max_length=255)
    http_host = models.CharField(max_length=255)
    favicon = models.ImageField(
        upload_to='assets/favicon/%Y/%m/',
        blank=True,
        default='',
        validators=[validate_png]
    )
    background = models.ImageField(
        upload_to='assets/background/%Y/%m/',
        blank=True,
        default='',
        validators=[validade_image]
    )
    login = models.BooleanField(default=True, verbose_name='Ativar Login')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True, verbose_name='Ativar Site')

    # @property
    # def section_about(self):
    #     return self.sectionabout_set.first()

    @property
    def section_videos(self):
        return self.video_set.filter(is_active=True)

    def save(self, *args, **kwargs):
        current_favicon_name = str(self.favicon.name)
        super().save(*args, **kwargs)
        favicon_changed = False
        if self.favicon:
            favicon_changed = current_favicon_name != self.favicon.name
        if favicon_changed:
            resize_image(self.favicon, 32)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Site Setup'
        verbose_name_plural = 'Site Setup'
