from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse,reverse_lazy

# Create your models here.


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    picture = models.ImageField(upload_to='profile_images', blank=True)
    bio = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self) -> str:
        return self.user.username
    
    def get_absolute_url(self):
        return reverse_lazy("profile", kwargs={"username": self.user.username})

        

class Comment(models.Model):
    pass


class Post(models.Model):
    pass