import re

from django import forms
from django.core.exceptions import ValidationError


class Lowercase(forms.CharField):
    def to_python(self, value):
        return value.lower()


class Titlecase(forms.CharField):
    def to_python(self, value):
        return value.title()


def email_validator(value):
    regex = re.compile(r"^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$")

    if not regex.match(value):
        raise ValidationError("E-mail inválido")


def strong_password(password):
    regex = re.compile(r"^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9]).{8,}$")

    if not regex.match(password):
        raise ValidationError(
            "As condições necessarias não foram atendidas. \
            Deve conter no mínimo 8 digitos, letas maiúsculas,\
            minúsculas e números."
        )
