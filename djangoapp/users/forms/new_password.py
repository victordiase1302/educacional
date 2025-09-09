from django import forms
# from django.contrib.auth import authenticate
# from django.core.exceptions import ValidationError
from users.models import User
from users.utils import for_forms as utils


class NewPassword(forms.ModelForm):
    class Meta:
        model = User
        fields = ('password',)

    def save(self, commit=True):
        user = super().save(commit=False)
        password = self.cleaned_data["password"]
        user.set_password(password)
        if commit:
            user.save()
        return user

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
