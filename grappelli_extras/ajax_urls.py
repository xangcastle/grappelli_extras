from django.conf.urls import url
from .ajax import *

# app_label = "grappelli_extras" fixme check before use app label

urlpatterns = [
    url(r'^get_object/', get_object, name="ajax_getObject"),
    url(r'^object_update/', object_update, name="ajax_ObjectUpdate"),
    url(r'^object_view/', object_view, name="ajax_ObjectView"),
    url(r'^get_collection/', get_collection, name="ajax_getCollection"),
    url(r'^get_datatables/', get_datatables, name="ajax_getDataTables"),
    url(r'^autocomplete/', autocomplete, name="ajax_autocomplete"),
    url(r'^object_execute/', object_execute, name="ajax_objectExecute"),
    url(r'^get_html_form/', get_html_form, name="ajax_getHtmlForm"),
]
