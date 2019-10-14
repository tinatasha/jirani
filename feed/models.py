from django.db import models
from django.utils import timezone
# Create your models here.
class Image(models.Model):
    image = models.ImageField(upload_to='images/')
    image_name = models.CharField(max_length=300)
    image_caption = models.TextField(max_length=500)
    likes = models.IntegerField(default=0)
    comments = models.TextField(blank=True, max_length=700)
    time = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return self.image_name
    
class Profile(models.Model):
    profile_photo = models.ImageField(upload_to="profile")
    bio = models.TextField(max_length=800)