from django.conf.urls import url
from .extras import *

urlpatterns = [
    url(r'^print/', to_print, name="extras_to_print"),
]
