import os
import boto3
from django.conf import settings
from django.db.models.signals import pre_delete, pre_save
from django.dispatch import receiver

from platforms.models import Platform


def delete_cover(instance):
    s3 = boto3.resource(
        's3',
        aws_access_key_id=settings.AWS_ACCESS_KEY_ID,
        aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY,
    )    
    
    bucket_name = settings.AWS_STORAGE_BUCKET_NAME
    file_key = instance.logo.name
    try:
        s3.Object(bucket_name, file_key).delete()        
    except Exception as e:
        print("------>", e, sep='\n')


@receiver(pre_delete, sender=Platform)
def recipe_cover_delete(sender, instance, *args, **kwargs):    
    old_instance = Platform.objects.filter(id=instance.id).first()
    logo_place_holder = "place_holder.png"
    name_cover = instance.logo.name
    if not name_cover == logo_place_holder:
        delete_cover(old_instance)

@receiver(pre_save, sender=Platform)
def recipe_cover_update(sender, instance, *args, **kwargs):
    old_instance = Platform.objects.filter(id=instance.id).first()

    if not old_instance:
        return
    
    if old_instance.logo:
        is_new_cover = old_instance.logo != instance.logo

        if is_new_cover:            
            delete_cover(old_instance)
