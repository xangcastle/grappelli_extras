from django.conf import settings


def extra_menus(request):
    return {'extra_menus': settings.EXTRA_MENUS}
