from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    class Role(models.TextChoices):
        ADMIN = "ADMIN", "Administrador"
        MANAGER = "MANAGER", "Manager"

    role = models.CharField(
        max_length=15,
        choices=Role.choices,
        null=True,
        blank=True,
    )
    email = models.EmailField(unique=True, verbose_name='E-mail', null=True)
    cell_phone = models.CharField(
        max_length=50, verbose_name='Celular', null=True
    )

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]

    def __str__(self):
        return self.email

    class Meta:
        app_label = "users"
        db_table = "users.user"
        verbose_name = "Usuario"
        verbose_name_plural = "Usuarios"
