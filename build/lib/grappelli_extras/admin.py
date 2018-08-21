from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from django.contrib.admin import site
import adminactions.actions as actions
actions.add_to_site(site)


class entidad_admin(ImportExportModelAdmin):
    list_display = ('code', 'name')
    ordering = ('-code',)



class documento_admin(admin.ModelAdmin):
    ordering = ('-number',)
    date_hierarchy = 'date'
    change_form_template = "print/document.html"
    printed_readonly_fields = ()
    only_superuserfields = ('date', 'number')
    def get_readonly_fields(self, request, obj=None):
        if request.user.is_superuser:
            return []
        if obj and obj.impreso:
            return self.printed_readonly_fields
        elif obj and obj.cliente:
            return self.only_superuserfields + ('name', 'phone', 'nit', 'address')
        else:
            return self.only_superuserfields



class document_detail(admin.TabularInline):
    extra = 0
    classes = ('grp-collapse grp-open',)
    exclude = ('blog', )
    inline_classes = ('grp-collapse grp-open',)
    printed_readonly_fields = []
    def get_readonly_fields(self, request, obj=None):
        if not request.user.is_superuser and obj:
            if obj.impreso:
                return self.printed_readonly_fields
        return self.readonly_fields