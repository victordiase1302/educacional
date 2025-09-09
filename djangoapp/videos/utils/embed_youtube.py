import re


def embed_youtube(url):
    embed = 'https://www.youtube.com/embed/'
    is_shortened = url.rfind('.be/')

    if is_shortened != -1:
        ft = url.split('.be/')
        url = f'{embed}{ft[1]}'
        return url

    ft = url.split('com/')
    verify = ft[1].rfind('?v=')
    if (verify != -1):
        slug = ft[1].split('v=')
        url = f'{embed}{slug[1]}'
        return url
    url = f'{embed}{ft[1]}'
    return url


def transform_to_embed_link(link):
    video_id = re.search(r'(?<=v=)[^&#]+', link)
    video_id = video_id[0] if video_id else None

    return f"https://www.youtube.com/embed/{video_id}" if video_id else link


def embed_video_youtube(url):
    # Expressões regulares para corresponder a diferentes formatos de URL
    padrao_completo = r'youtube\.com/watch\?v=([a-zA-Z0-9_-]+)'
    padrao_encurtado = r'youtu\.be/([a-zA-Z0-9_-]+)'
    padrao_embed = r'youtube\.com/embed/([a-zA-Z0-9_-]+)'
    padrao_live = r'youtube\.com/live/([a-zA-Z0-9_-]+)'  # Padrão para URLs de live

    # Procura pelo padrão correspondente na URL
    match = re.search(padrao_completo, url) or \
            re.search(padrao_encurtado, url) or \
            re.search(padrao_embed, url) or \
            re.search(padrao_live, url)

    if match:
        video_id = match.group(1)
        return f'https://www.youtube.com/embed/{video_id}'
    else:
        return url
