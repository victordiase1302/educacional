from django.core.exceptions import ValidationError


def validate_png(image):
    if not image.name.lower().endswith('.png'):
        raise ValidationError('Imagem precisa ser PNG')


def validade_image(image):
    valid_extensios = ['png', 'jpg', 'jpeg', 'svg']
    name_file = image.name.lower()
    extension = name_file.split('.')[-1]
    if extension not in valid_extensios:
        raise ValidationError('Apenas imagens são permitidas')
