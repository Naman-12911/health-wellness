from django.urls import path
from .views import ListingsApiview,ListingSearchView,CartAPIView

urlpatterns = [
    path('get-listing/', ListingsApiview.as_view(), name='ListingsApiview'),
    path('get-listing/<int:pk>/', ListingsApiview.as_view(), name='ListingsApiview'),
    path('cart/', CartAPIView.as_view(), name='CartAPIView'),
    path('cart/<int:pk>/', CartAPIView.as_view(), name='CartAPIView'),
    path('search/', ListingSearchView.as_view(), name='ListingSearchView'),
]