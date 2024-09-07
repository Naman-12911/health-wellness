from django.shortcuts import render

from listing.serializer import ListingsSerializer
from .models import Listing
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http.response import Http404
from rest_framework import status
from rest_framework import generics
from .filters import ListingFilters
import django_filters
from rest_framework.filters import SearchFilter

# Create your views here.
class ListingsApiview(APIView):
    permission_classes = [IsAuthenticated]
    def get_object(self, pk):
        try:
            return Listing.objects.get(pk=pk)
        except Listing.DoesNotExist:
            raise Http404
        # get the employee by id otherwise all the employee
    def get(self, request, pk=None, format=None):
        if pk:
            listing = self.get_object(pk)
            if listing.is_published:
                serializer = ListingsSerializer(listing,context={'request': request})
                return Response(serializer.data)
            else:
                return Response({'detail': 'House not found or not published.'}, status=status.HTTP_404_NOT_FOUND)

        else:
            data = Listing.objects.filter(is_published=True)
            serializer = ListingsSerializer(data, many=True,context={'request': request})
            return Response(serializer.data)
        

# search feture ------------------------------------


class ListingSearchView(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Listing.objects.all()
    serializer_class = ListingsSerializer
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend, SearchFilter]
    filterset_class = ListingFilters
    search_fields = ['title', 'city', 'state', 'bedrooms','bathrooms','garden','garage','description','price']


    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        
        if not queryset.exists():
            return Response({'detail': 'No data found'}, status=status.HTTP_204_NO_CONTENT)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)






