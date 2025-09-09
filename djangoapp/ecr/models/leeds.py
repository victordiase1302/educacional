from django.db import models
import uuid


class Lead(models.Model):
    pkid = models.BigAutoField(primary_key=True, editable=False)
    uid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    first_name = models.CharField(
        max_length=150,
        verbose_name="Nome",
        null=True,
    )
    email = models.EmailField(
        max_length=150,
        unique=True,
        verbose_name="E-mail",
    )
    message = models.TextField(blank=True, null=True, verbose_name="Observação")
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Criado em",
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name="Atualizado em",
    )
    is_active = models.BooleanField(default=True, verbose_name="Leed ativo")

    def __str__(self):
        return self.email

    class Meta:
        ordering = ("-updated_at",)
        verbose_name = "Leed"
        verbose_name_plural = "Leeds"
