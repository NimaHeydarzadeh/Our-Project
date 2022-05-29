from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse, reverse_lazy
from django.template.defaultfilters import slugify

# Create your models here.


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # picture = models.ImageField(upload_to='profile_images', blank=True)
    bio = models.CharField(max_length=200, blank=True, null=True)
    create_date = models.DateTimeField(auto_now_add=True,null = True)
    modify_date = models.DateTimeField(auto_now=True,null = True)

    def __str__(self):
        return self.user.username

    def get_absolute_url(self):
        return reverse_lazy("profile", kwargs={"username": self.user.username})


class Post(models.Model):
   
    slug = models.SlugField(max_length=100, blank=True)
    auth = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    create_date = models.DateTimeField(auto_now_add=True,null = True)
    modify_date = models.DateTimeField(auto_now=True,null = True)
    title = models.CharField(max_length=200)
    body = models.TextField()
    date = models.DateField(auto_now_add=True)
    like = models.ManyToManyField(UserProfile, related_name="post_like")
    dislike = models.ManyToManyField(UserProfile, related_name="post_dislike",blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            slug = f"{self.id}-{slugify(self.title)}"
            self.slug = slug
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("post", kwargs={"slug": self.slug})
