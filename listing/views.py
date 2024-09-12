from django.shortcuts import render

from listing.serializer import ListingsSerializer,CartSerializer
from .models import Listing,Cart
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

class CartAPIView(APIView):
    permission_classes = [IsAuthenticated]
    def get_object(self, pk):
        try:
            return Cart.objects.get(pk=pk)
        except Cart.DoesNotExist:
            raise Http404
    def get(self, request, pk=None, format=None):
        current_user = request.user
        if pk:
            data = self.get_object(pk)
            serializer = CartSerializer(data)
            return Response(serializer.data)
        else:
            data = Cart.objects.filter(user=current_user)
            serializer = CartSerializer(data, many=True)
            if not data.exists():
                return Response({'detail': 'Get all cart items'}, status=status.HTTP_404_NOT_FOUND)
            return Response(serializer.data)
    def post(self, request, format=None):
            current_user = request.user
            mutable_data = request.data.copy()
            mutable_data['user'] = current_user.id 
            
            serializer = CartSerializer(data=mutable_data)

            # Check if the data passed is valid
            serializer.is_valid(raise_exception=True)
            serializer.save()
            # Return Response to User

            response = Response()

            response.data = {
                'message': 'cart Created Successfully',
                'data': serializer.data
            }
            return response


