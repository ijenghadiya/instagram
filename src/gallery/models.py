from django.db import models
from django.contrib.auth import get_user_model
    

class Album(models.Model):
    name = models.CharField(max_length=120, blank=False, null=False)
    submitter = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    description = models.TextField(max_length=500, null=True)
    images = models.ManyToManyField("Image", related_name="album_images", blank=True)
    tags = models.ManyToManyField("Tag", related_name="all_tags", blank=True)
    is_public = models.BooleanField(default=False)
    timestamp = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)

    def __str__(self):
        return str(self.submitter)

class Image(models.Model):
    name        = models.CharField(max_length=120, blank=False, null=False)
    album       = models.ForeignKey("Album", related_name="album_id", null=True, blank=True, on_delete=models.CASCADE)
    image       = models.ImageField(verbose_name="Image", blank=True, null=True, upload_to='img')
    timestamp   = models.DateField(auto_now_add=True)
    updated     = models.DateField(auto_now=True)

    def __str__(self):
        return self.name

class Tag(models.Model):
    name = models.CharField(max_length=120, blank=False, null=False)
    albums = models.ManyToManyField("Album", blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Caption(models.Model):
    caption = models.TextField(max_length=500, null=True, blank=False)
    fontcolor = models.TextField(max_length=500, null=True)
    image = models.OneToOneField("Image", related_name="image_id", null=True, blank=True, on_delete=models.CASCADE)
    position_x = models.IntegerField(null=True, blank=True)
    position_y = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.caption

