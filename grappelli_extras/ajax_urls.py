from django.urls import path
from .ajax import *

app_name = "grappelli_extras"

urlpatterns = [
    path('get_object/', get_object, name="ajax_getObject"),
    path('object_update/', object_update, name="ajax_ObjectUpdate"),
    path('object_view/', object_view, name="ajax_ObjectView"),
    path('get_collection/', get_collection, name="ajax_getCollection"),
    path('get_datatables/', get_datatables, name="ajax_getDataTables"),
    path('autocomplete/', autocomplete, name="ajax_autocomplete"),
    path('object_execute/', object_execute, name="ajax_objectExecute"),
    path('get_html_form/', get_html_form, name="ajax_getHtmlForm"),
]
