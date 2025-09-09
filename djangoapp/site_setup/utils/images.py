from pathlib import Path

from django.conf import settings
from PIL import Image


def resize_image(image_django, new_with=800, optimize=True, quality=60):
    image_path = Path(settings.MEDIA_ROOT / image_django.name).resolve()
    image_pillow = Image.open(image_path)
    original_width, original_height = image_pillow.size

    if original_width <= new_with:
        image_pillow.close()
        return image_pillow

    new_height = round(new_with * original_height / original_width)

    new_image = image_pillow.resize((new_with, new_height), Image.LANCZOS)
    new_image.save(image_path, optimize=optimize, quality=quality)
    return new_image


def resize_logo_nav(
    image_django, max_with=400, max_heig=70, optimize=True, quality=60
):
    image_path = Path(settings.MEDIA_ROOT / image_django.name).resolve()
    image_pillow = Image.open(image_path)
    original_width, original_height = image_pillow.size
    offset = (
        max_with, max_heig
    )

    new_image = image_pillow.resize(offset, Image.LANCZOS)
    new_image.save(image_path, optimize=optimize, quality=quality)
    return new_image
