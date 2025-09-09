import boto3
from django.conf import settings
from django.db import models
from django.utils.text import slugify


class EbookDownload(models.Model):
    title = models.CharField(max_length=255, null=True, blank=True)
    user_agent = models.CharField(max_length=500, null=True, blank=True)
    ip_address = models.GenericIPAddressField(null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Download do Ebook"
        verbose_name_plural = "Downloads do Ebook"

    def __str__(self):
        return f"Download em {self.timestamp}"


class ArquivoS3(models.Model):
    titulo = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True, blank=True)
    arquivo = models.FileField(upload_to="uploads/")
    chave_s3 = models.CharField(max_length=255, blank=True)
    data_upload = models.DateTimeField(auto_now_add=True)
    tipo_arquivo = models.CharField(max_length=100, blank=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Upload de Arquivo"
        verbose_name_plural = "Uploads de Arquivos"

    def __str__(self):
        return self.titulo

    def _gerar_slug_unico(self):
        slug = slugify(self.titulo)
        slug_unico = slug
        num = 1

        # Enquanto existir um slug igual, adiciona um número ao final
        while ArquivoS3.objects.filter(slug=slug_unico).exists():
            slug_unico = f"{slug}-{num}"
            num += 1

        return slug_unico

    def save(self, *args, **kwargs):
        # Gera o slug se não existir
        if not self.slug:
            self.slug = self._gerar_slug_unico()

        # Primeiro salva o modelo para ter o arquivo disponível
        super().save(*args, **kwargs)

        if self.arquivo and not self.chave_s3:
            # Configura o cliente S3
            s3_client = boto3.client(
                "s3",
                aws_access_key_id=settings.AWS_ACCESS_KEY_ID,
                aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY,
                region_name=settings.AWS_REGION_NAME,
            )

            # Define a chave do arquivo no S3 usando o slug
            self.chave_s3 = f"{self.arquivo.name}"

            # Faz o upload para o S3
            s3_client.upload_fileobj(
                self.arquivo.file, "econometriafacil", self.chave_s3
            )

            # Salva novamente para atualizar a chave_s3 e tipo_arquivo
            super().save(*args, **kwargs)
