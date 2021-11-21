from rest_framework import serializers
from django.contrib.auth.models import User
from gallery.models import Album, Image, Tag, Caption

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username']

class AlbumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Album
        fields = ['id', 'name', 'description', 'images', 'submitter', 'tags', 'is_public', 'timestamp', 'updated']

class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = '__all__'

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'

class CaptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Caption
        fields = '__all__'