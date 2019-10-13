from django.db import models

# Create your models here.
class Image(models.Model):
    image = models.ImageField(upload_to="images")
    image_name = models.CharField(max_length=300)
    image_caption = models.TextField(max_length=500)
    likes = models.IntegerField(default=0)
    comments = models.TextField(max_length=700)
    
class Profile(models.Model):
    profile_photo = models.ImageField(upload_to="profile")
    bio = models.TextField(max_length=800)