from rest_framework.serializers import  ModelSerializer
from .models import Listing,Cart
from django.contrib.sites.shortcuts import get_current_site
from account.serializer import UserSerializers


class ListingsSerializer(ModelSerializer):
    class Meta:
        model = Listing
        fields = "__all__"
    def photo_1Image(self, obj):
        return self.build_absolute_image_url(obj.photo_1)
    def photo_2Image(self, obj):
        return self.build_absolute_image_url(obj.photo_2)
    
    def photo_3Image(self, obj):
        return self.build_absolute_image_url(obj.photo_3)
    
    def photo_4Image(self, obj):
        return self.build_absolute_image_url(obj.photo_4)
    def photo_5Image(self, obj):
        return self.build_absolute_image_url(obj.photo_5)

    def build_absolute_image_url(self, image_path):
        request = self.context.get('request')
        if request is not None:
            return request.build_absolute_uri(image_path)
        else:
            # If request is not available (for example, in shell), use the default site
            site = get_current_site(None)
            return f"{site.scheme}://{site.domain}{image_path}"
        
        
class CartSerializer(ModelSerializer):
    class Meta:
        model = Cart
        fields = "__all__"
    def to_representation(self, instance):
        response = super().to_representation(instance)
        response['product'] = ListingsSerializer(instance.product).data
        response['user'] = UserSerializers(instance.user).data
        
        return response