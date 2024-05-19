from rest_framework import serializers
from .models import Picture
from rest_framework.parsers import FileUploadParser


# Converts Picture model instances to JSON
class PictureSerializer(serializers.ModelSerializer):
    # Defines the PictureSerializer behaviour
    class Meta:
        model = Picture
        fields = ['id', 'name', 'email', 'group_image']
        parser_class = (FileUploadParser,)