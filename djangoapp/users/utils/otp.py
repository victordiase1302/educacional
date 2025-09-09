import random

import boto3
from decouple import config
from django.core.cache import cache


def send_otp(phone_number):
    otp = random.randint(100000, 999999)  # Gere um OTP de 6 dígitos

    sns = boto3.client(
        'sns',
        aws_access_key_id=config("AWS_ACCESS_KEY_ID"),
        aws_secret_access_key=config("AWS_SECRET_ACCESS_KEY"),
        region_name='us-east-1'
    )

    sns.publish(
        PhoneNumber=phone_number,
        Message=f'Daniel Fortune: seu código de verificação é {otp}'
    )
    print(phone_number, otp)
    # sns.create_sms_sandbox_phone_number(
    #     PhoneNumber=phone_number,
    #     LanguageCode='pt-BR'
    # )
    return otp


def verify_otp(phone_number, user_otp):
    otp = cache.get(phone_number)  # Recupera o OTP do cache
    return otp == user_otp
