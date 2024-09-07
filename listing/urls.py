from django.urls import path
from .views import ListingsApiview,ListingSearchView

urlpatterns = [
    path('get-listing/', ListingsApiview.as_view(), name='ListingsApiview'),
    path('get-listing/<int:pk>/', ListingsApiview.as_view(), name='ListingsApiview'),
    path('search/', ListingSearchView.as_view(), name='ListingSearchView'),
]