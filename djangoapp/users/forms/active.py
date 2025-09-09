from django import forms

# from django.contrib.auth.forms import SetPasswordForm


class ActiveUserForm(forms.Form):
    def __init__(self, user, *args, **kwargs):
        self.user = user
        super().__init__(*args, **kwargs)

    def save(self, commit=True):
        self.user.is_active = True
        if commit:
            self.user.save()
        return self.user
