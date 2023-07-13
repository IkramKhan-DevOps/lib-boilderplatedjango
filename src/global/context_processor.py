
from .models import SiteSettings


def site_settings(request):
    try:
        settings, created = SiteSettings.objects.get_or_create()
    except SiteSettings.DoesNotExist:
        settings = None

    return {'sc_site': settings}
