from django.contrib import admin
from django.utils.translation import gettext_lazy  as _
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from .models import User
from  django.contrib.auth.models  import  Group
from import_export.admin import ImportExportModelAdmin
class customUserAdmin(UserAdmin,ImportExportModelAdmin):
  #form = UserChangeForm
  fieldsets = (
      (None, {'fields': ('email', 'password', )}),
      (_('Personal info'), {'fields': ('name', 'state','country','address')}),
      (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser',
                                     'groups', 'user_permissions'),}),
      (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
        (_('user_info'), {'fields': ( 'phone_no',)}),
  )
  add_fieldsets = (
      (None, {
          'classes': ('wide', ),
          'fields': ('email', 'password1', 'password2'),
      }),
  )
  list_display = ['email', 'name', 'is_staff' ,"phone_no",]
  search_fields = ('email',)
  ordering = ('email', )
admin.site.register(User, customUserAdmin)


admin.site.unregister(Group)