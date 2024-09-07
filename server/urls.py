
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import PasswordResetView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('account/',include('account.urls')), # account app urls
    path('listing/',include('listing.urls')), # listings app urls
    path('booking/',include('bookings.urls')), # house tour app urls
    path('password_reset/', PasswordResetView.as_view(), name='password_reset'),
    

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


admin.site.site_header = 'Health and Wellness Products'
admin.site.site_title = 'Health and Wellness Products'
admin.site.index_title = 'Health and Wellness Products'
