from rest_framework import serializers
from .models import Picture

# Converts Picture model instances to JSON
class PictureSerializer(serializers.ModelSerializer):
    # Defines the PictureSerializer behaviour
    class Meta:
        model = Picture
        fields = ['id', 'name', 'description']