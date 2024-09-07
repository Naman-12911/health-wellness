from django.contrib import admin
from .models import *
from import_export.admin import ImportExportModelAdmin
# Register your models here.

class BookingAdmin(ImportExportModelAdmin):
    list_display = ('listing','name','phone_no','email')

class paymentAdmin(ImportExportModelAdmin):
    list_display=("booking","price","status","user",)
    search_fields=("booking","price","status","user",)


class ContactAdmin(ImportExportModelAdmin):
    list_display=("user","email","name",)
    search_fields=("user","email","name",)
admin.site.register(Booking,BookingAdmin)
admin.site.register(ContactUs,ContactAdmin)
admin.site.register(HelpTransportation)
admin.site.register(payment,paymentAdmin)