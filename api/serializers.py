from rest_framework import serializers
from .models import  Item


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ('__all__')


# class LocationSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Location
#         fields = ('__all__')



class FileUploadSerializer(serializers.Serializer):
    file = serializers.FileField()
    
class SaveFileSerializer(serializers.Serializer):
    
    class Meta:
        model = Item
        fields = "__all__"