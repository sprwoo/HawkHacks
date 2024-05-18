from .models import Picture
from .serializers import PictureSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

@api_view(['GET', 'POST'])
def picture_list(request):
    if request.method == 'GET':
        pictures = Picture.objects.all()
        serializer = PictureSerializer(pictures, many=True)
        return Response(serializer.data) 
    if request.method == 'POST':
        serializer = PictureSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
@api_view(["GET", "PUT", "DELETE"])
def picture_detail(request, id):
    try:
        picture = Picture.objects.get(pk=id)
    except Picture.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == "GET":
        serializer = PictureSerializer(picture)
        return Response(serializer.data)
    elif request.method == "PUT":
        serializer = PictureSerializer(picture, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        picture.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
