import re

from django.core.cache import cache
from django.shortcuts import render
from users.forms import RegisterUserForm
from users.models import User
from users.utils.format_number import format_numbers
from users.utils.otp import send_otp

# from users.services import send_mail_to_user


def register(request, *args, **kwargs):
    if request.method == 'GET':
        return render(request, 'users/register.html')
    if request.method == 'POST':
        form = RegisterUserForm(request.POST or None)
        if form.is_valid():
            user = form.save()
            # send_mail_to_user(request=request, user=user)
            number = re.sub(r"\D", "", user.cell_phone)
            cod_otp = send_otp(phone_number=f"+55{number}")
            cache.set(
                f"+55{number}",
                {"cod_otp": str(cod_otp), "user_obj": user},
                60 * 15
            )
            return render(
                request,
                "users/otp-cad-confirm.html",
                {"cell_phone": number}
            )
        print(form.errors)
        response = render(request, 'users/register.html', {'form': form})
        response["HX-Retarget"] = "#main"
        return response


def verify_register_otp(request, *args, **kwargs):
    if request.method == "POST":
        digits, cell_phone = format_numbers(request.POST)
        otp_code = cache.get(f"+55{cell_phone}")
        if digits != otp_code["cod_otp"]:
            message = "Código inválido"
            return render(
                request,
                "users/otp-cad-confirm.html",
                {
                    "message": message,
                    'type': 'danger'
                }
            )
        user_obj = User.objects.get(email=otp_code["user_obj"])
        user_obj.is_active = True
        user_obj.save()
        message = 'Conta ativada com sucesso!'
        return render(
            request,
            'users/login.html',
            {
                'message': message,
                'type': 'success'
            }
        )


def login(request, *args, **kwargs):
    return render(request, 'users/login.html')
