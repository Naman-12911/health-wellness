from django.contrib import admin
from .models import *
from import_export.admin import ImportExportModelAdmin
# Register your models here.


class ListingAdmin(ImportExportModelAdmin):
    list_display = ("title","id")
    search_fields = ("title",)

admin.site.register(Listing,ListingAdmin)
admin.site.register(Cart)
