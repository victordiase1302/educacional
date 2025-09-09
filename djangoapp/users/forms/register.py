from django import forms
from django.core.exceptions import ValidationError
from users.models import User
from users.utils import for_forms as utils


class RegisterUserForm(forms.ModelForm):
    first_name = utils.Titlecase(
        error_messages={"required": "Por favor digite um nome válido"},
        required=True,
        label='Nome',
        max_length=150,
    )
    cell_phone = forms.CharField(
        error_messages={"required": "Por favor digite um sobrenome válido"},
        required=True,
        label='Celular',
        max_length=150,
    )
    email = utils.Lowercase(
        error_messages={"required": "Por favor digite um email válido"},
        label='E-mail',
        required=True,
        validators=[utils.email_validator],
    )
    password = forms.CharField(
        required=True,
        label="Senha",
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "Digite sua senha",
                "id": "dz-password",
            },
        ),
        validators=[utils.strong_password],
        min_length=8,
    )

    class Meta:
        model = User
        fields = (
            'first_name',
            'cell_phone',
            'email',
            'password'
        )

    def save(self, commit=True):
        user = super().save(commit=False)
        user.username = self.cleaned_data["email"]
        password = self.cleaned_data["password"]
        user.set_password(password)
        user.is_active = False
        if commit:
            user.save()
        return user

    def clean_email(self):
        email = self.cleaned_data.get("email")
        if _ := User.objects.filter(email=email).exists():
            raise ValidationError("E-mail já em uso", code="invalid")
        return email

    def clean_cell_phone(self):
        cell_phone = self.cleaned_data.get("cell_phone")
        if _ := User.objects.filter(cell_phone=cell_phone).exists():
            raise ValidationError(
                "Número de telefone já em uso", code="invalid"
            )
        return cell_phone
