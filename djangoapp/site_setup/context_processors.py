from site_setup.models import SiteSetup


def site_setup(request):
    host = request.META.get('HTTP_HOST', '')
    if host.startswith('www.'):
        host = host[4:]
    # if host == 'danielfortune.com.br':
    #     host = 'danielrendacomjogos.com.br'
    # if host == 'desenvolvimento.danielfortune.com.br':
    #     host = 'desenvolvimento.danielrendacomjogos.com.br'
    data = SiteSetup.objects.filter(http_host=host).first()
    return {
        'site_setup': data
    }
