import re

from django.contrib.auth.views import (PasswordResetCompleteView,
                                       PasswordResetConfirmView,
                                       PasswordResetDoneView,
                                       PasswordResetView)
from django.core.cache import cache
from django.core.exceptions import ValidationError
from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.utils.http import urlsafe_base64_decode
from users.forms import ActiveUserForm, NewPassword
from users.models import User
from users.utils.format_number import format_numbers
from users.utils.otp import send_otp


def forgot_password(request, *args, **kwargs):
    if request.method == "GET":
        return render(request, "users/forgot-password.html")
    if request.method == "POST":
        cell_phone = request.POST.get("cell_phone")
        if User.objects.filter(cell_phone=cell_phone).exists():
            return _generate_forgot_password(request, cell_phone)
        message = "Número incorreto"
        return render(
            request,
            "users/forgot-password.html",
            {
                "message": message,
                'type': 'danger'
            }
        )


# TODO Rename this here and in `forgot_password`
def _generate_forgot_password(request, cell_phone):
    user_obj = User.objects.filter(cell_phone=cell_phone).first()
    number = re.sub(r"\D", "", cell_phone)
    cod_otp = send_otp(phone_number=f"+55{number}")
    cache.set(
        f"+55{number}",
        {"cod_otp": str(cod_otp), "user_obj": user_obj},
        60 * 15
    )
    print(cell_phone, cod_otp, sep="\n")
    return render(
        request, "users/otp-recovery-confirm.html", {"cell_phone": number}
    )


def verify_otp(request, *args, **kwargs):
    if request.method == "POST":
        digits, cell_phone = format_numbers(request.POST)
        otp_code = cache.get(f"+55{cell_phone}")
        # print(otp_code["cod_otp"], digits, "!!!", sep="\n")
        if digits != otp_code["cod_otp"]:
            message = "Código inválido"
            return render(
                request,
                "users/otp-recovery-confirm.html",
                {
                    "message": message,
                    'type': 'danger'
                }
            )
        return render(
            request,
            "users/form-recovery-password.html",
            {"user": otp_code["user_obj"]}
        )


def change_password(request, *args, **kwargs):
    if request.method == "POST":
        print(request.POST.get("user"))
        if user := request.POST.get("user"):
            instance = User.objects.get(email=user)
            print(instance)
            form = NewPassword(request.POST, instance=instance)
            if form.is_valid():
                form.save()
                message = 'Senha alterada com sucesso!'
                return render(
                    request,
                    'users/login.html',
                    {
                        'message': message,
                        'type': 'success'
                    }
                )
        print(form.errors)
    return render(
        request,
        "users/form-recovery-password.html",
        {
            "message": form.errors,
            'type': 'danger',
            'user': user
        }
    )


class MyPasswordResetConfirm(PasswordResetConfirmView):
    template_name = "users/account/password_reset_confirm.html"
    success_url = reverse_lazy("users:reset_password_complete_done")
    form_class = ActiveUserForm

    def get_user(self, uidb64):
        try:
            uid = urlsafe_base64_decode(uidb64).decode()
            user = User._default_manager.get(pk=uid)
        except (
            TypeError,
            ValueError,
            OverflowError,
            User.DoesNotExist,
            ValidationError,
        ):
            user = None
        return user

    def form_valid(self, form):
        self.user.is_active = True
        self.user.save()
        return super(MyPasswordResetConfirm, self).form_valid(form)


class MyPasswordResetComplete(PasswordResetCompleteView):
    template_name = "users/account/password_send_mensage.html"


class MyPasswordReset(PasswordResetView):
    template_name = "users/account/forgot_password.html"
    success_url = reverse_lazy("users:reset_password_requested_done")
    email_template_name = "users/account/account_activation_email.html"
    # form_class = ForgotPasswordForm


class MyPasswordResetDone(PasswordResetDoneView):
    template_name = "users/account/password_reset_done.html"
