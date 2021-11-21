from django.shortcuts import get_object_or_404, render
from django.contrib.auth.models import User
from rest_framework import generics
from gallery import serializers
from django.contrib.auth.models import User
from gallery.models import Album, Image, Tag, Caption

class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer

class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer

class AlbumList(generics.ListCreateAPIView):
    queryset = Album.objects.all()
    serializer_class = serializers.AlbumSerializer


class AlbumDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Album.objects.all()
    serializer_class = serializers.AlbumSerializer

class ImageList(generics.ListCreateAPIView):
    queryset = Image.objects.all()
    serializer_class = serializers.ImageSerializer

class ImageDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Image.objects.all()
    serializer_class = serializers.ImageSerializer

class TagList(generics.ListCreateAPIView):
    queryset = Tag.objects.all()
    serializer_class = serializers.TagSerializer

class TagDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Tag.objects.all()
    serializer_class = serializers.TagSerializer

class CaptionList(generics.ListCreateAPIView):
    queryset = Caption.objects.all()
    serializer_class = serializers.CaptionSerializer

class CaptionDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Caption.objects.all()
    serializer_class = serializers.CaptionSerializer

class UserAlbumList(generics.ListAPIView):
    serializer_class = serializers.AlbumSerializer
    

    def get_queryset(self):
        user = get_object_or_404(User, id=self.kwargs.get('id'))
        return Album.objects.filter(submitter=user)
