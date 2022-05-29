from xml.etree.ElementTree import Comment
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse, reverse_lazy
from django.template.defaultfilters import slugify
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation

# Create your models here.


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # picture = models.ImageField(upload_to='profile_images', blank=True)
    bio = models.CharField(max_length=200, blank=True, null=True)
    create_date = models.DateTimeField(auto_now_add=True, null=True)
    modify_date = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return self.user.username

    def get_absolute_url(self):
        return reverse_lazy("profile", kwargs={"username": self.user.username})


class Comment(models.Model):
    body = models.TextField()
    date_create = models.DateTimeField(auto_now_add=True)
    date_modify = models.DateTimeField(auto_now=True)
    # post = models.ForeignKey(
    #     "Post", on_delete=models.CASCADE)
    comment = GenericRelation("Comment")
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')

    auther = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    like = models.ManyToManyField(
        UserProfile, related_name="comment_likes")
    dislike = models.ManyToManyField(
        UserProfile, related_name='comment_dislikes')

    def get_absolute_url(self):
        return reverse("post", kwargs={"post_slug": self.post.slug})+f"#{self.pk}"


class Post(models.Model):

    slug = models.SlugField(max_length=100, blank=True)
    auth = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    create_date = models.DateTimeField(auto_now_add=True, null=True)
    modify_date = models.DateTimeField(auto_now=True, null=True)
    title = models.CharField(max_length=200)
    body = models.TextField()
    date = models.DateField(auto_now_add=True)
    like = models.ManyToManyField(UserProfile, related_name="post_like")
    dislike = models.ManyToManyField(
        UserProfile, related_name="post_dislike", blank=True)
    comment = models.ManyToManyField(Comment, blank=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            slug = f"{self.id}-{slugify(self.title)}"
            self.slug = slug
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("post", kwargs={"slug": self.slug})
