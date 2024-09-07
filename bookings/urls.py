from django.urls import path
from .views import *

urlpatterns = [
    path('contact/', ContactUsAPIView.as_view(), name='ContactUsAPIView'),
    path('booking/', BookingAPIView.as_view(), name='BookingAPIView'),
    path('booking/<int:pk>/', BookingAPIView.as_view(), name='BookingAPIView'),
    path('payment/', PaymentAPIView.as_view(), name='PaymentAPIView'),
    path('payment/<int:booking_id>/', PaymentAPIView.as_view(), name='PaymentAPIView'),

]