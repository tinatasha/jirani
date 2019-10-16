from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
# Create your models here.

class Image(models.Model):
    image = models.ImageField(upload_to='images/')
    image_name = models.CharField(max_length=300)
    image_caption = models.TextField(max_length=500)
    likes = models.IntegerField(default=0)
    comments = models.TextField(blank=True, max_length=700)
    time = models.DateTimeField(default=timezone.now)
    
    @classmethod
    def search_results(cls, search_term):
        images = cls.objects.filter(image_name__icontains=search_term)
        return images
    
    def __str__(self):
        return self.image_name

    
class UserProfile(models.Model):
    user = models.OneToOneField(User, unique=True, related_name="profile", on_delete=models.CASCADE)
    photo = models.ImageField(
        upload_to="images/", max_length=255, null=True, blank=True, default=""
    )
    phone = models.DecimalField(max_digits=10, decimal_places=0, default=0)
    bio = models.TextField()
    
    def __str__(self):
        return self.user.username
    
@receiver(post_save, sender=User)
def update_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)
    instance.profile.save()
