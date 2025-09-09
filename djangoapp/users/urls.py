from django.urls import path
from users import views as v

app_name = 'users'

urlpatterns = [
    path(
        "redefinicao-senha/<uidb64>/<token>/",
        v.MyPasswordResetConfirm.as_view(),
        name="reset_password_confirm"
    ),
    path('forgot-password/', v.forgot_password, name='forgot-password'),
    path('trocar-senha/', v.change_password, name='change-password'),
    path('verify-otp/', v.verify_otp, name='verify-otp'),
    path(
        'verify-register-otp/',
        v.verify_register_otp,
        name='verify-register-otp'
    ),
    path(
        "redefinicao-senha-confirmada/",
        v.MyPasswordResetDone.as_view(),
        name="reset_password_complete_done"
    ),
    path(
        "redefinicao-senha-solicitada/",
        v.MyPasswordResetComplete.as_view(),
        name="reset_password_requested_done"
    ),
    path(
        "resetar-senha/",
        v.MyPasswordReset.as_view(),
        name="reset_password"
    ),
    path('register/', v.register, name='register'),
    path('login/', v.login, name='login'),
]
