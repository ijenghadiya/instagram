from django.contrib import admin
from gallery.models import Album, Image, Tag

admin.site.register(Album)
admin.site.register(Image)
admin.site.register(Tag)