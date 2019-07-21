from django.contrib import admin
from .models import *
from import_export.admin import ImportExportModelAdmin


@admin.register(Customer)
class CustomerAdmin(ImportExportModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'country', 'region', 'city')
    search_fields = ('first_name', 'last_name', 'email', 'country', 'region', 'city')
    list_filter = ('country', 'region', 'city')

    fieldsets = (
        ('Customer Data', {
            'classes': ('grp-collapse', 'grp-open'),
            'fields': (('first_name', 'last_name'),
                       ('email', 'country'), ('region', 'city'))
        }),
    )

    change_form_template = "app/person.html"