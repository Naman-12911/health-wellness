from rest_framework.serializers import  ModelSerializer
from .models import *
from account.serializer import UserSerializers
from listing.models import Listing
from listing.serializer import ListingsSerializer

class BookingSerializer(ModelSerializer):
    class Meta:
        model = Booking
        fields = "__all__"
    def to_representation(self, instance):
        response = super().to_representation(instance)
        response['listing'] = ListingsSerializer(instance.listing).data
        response['user'] = UserSerializers(instance.user).data
        
        return response



class ContactusSerializer(ModelSerializer):
    class Meta:
        model = ContactUs
        fields = "__all__"


class HelpInTransportationSerializer(ModelSerializer):
    class Meta:
        model = HelpTransportation
        fields = "__all__"




class PaymentSerializer(ModelSerializer):
    class Meta:
        model = payment
        fields = "__all__"
