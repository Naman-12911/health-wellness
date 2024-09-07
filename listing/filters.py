import django_filters
from .models import Listing

class ListingFilters(django_filters.FilterSet):
   class Meta:
        model = Listing
        fields = {
            'title': ['exact'],
            # 'city': ['exact'],
            # 'state': ['icontains'],
            # 'bedrooms': ['exact'],
            # 'bathrooms': ['exact'],
            # 'garden': ['exact'],
            # 'garage': ['exact'],
            'description': ['icontains'],
            'price': ['lte'],
        }

