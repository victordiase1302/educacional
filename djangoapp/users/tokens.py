from django.contrib.auth.tokens import PasswordResetTokenGenerator

# from six import text_type


class AccountActivationTokenGenerator(PasswordResetTokenGenerator):
    pass


account_activation_token = AccountActivationTokenGenerator()
