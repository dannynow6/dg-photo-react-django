from django.shortcuts import render
from .models import Photo
from .serializers import PhotoSerializer
from rest_framework import viewsets

# Views for backend_api
class PhotoViewSet(viewsets.ModelViewSet):
    serializer_class = PhotoSerializer
    queryset = Photo.objects.all()
