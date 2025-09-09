from django import forms
from django.contrib.auth import authenticate
from django.core.exceptions import ValidationError


class LoginForm(forms.Form):
    username = forms.CharField(
        required=True,
        label="E-mail",
        widget=forms.EmailInput(
            attrs={
                "type": "email",
                "placeholder": "Digite e-mail cadastrado",
                "id": "register-username",
            }
        ),
    )
    password = forms.CharField(
        required=True,
        label="Senha",
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "Digite sua senha",
                "id": "register-password",
            },
        ),
    )

    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get("username")
        password = cleaned_data.get("password")
        self.user_cache = authenticate(
            username=username,
            password=password,
        )
        if self.user_cache is None:
            raise ValidationError(
                {
                    "username": "E-mail ou senha inválido.",
                    "password": "E-mail ou senha inválido.",
                }
            )
        return cleaned_data

    def get_user(self):
        print(self.user_cache, '<<<<<<<')
        return self.user_cache
