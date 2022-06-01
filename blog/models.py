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
    picture = models.ImageField(upload_to='profile_images', blank=True)
    bio = models.CharField(max_length=200, blank=True, null=True)
    create_date = models.DateTimeField(auto_now_add=True, null=True)
    modify_date = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        s = "User:  {}"
        return s.format(self.user.username)

    def get_absolute_url(self):
        return reverse_lazy("profile", kwargs={"username": self.user.username})


class Comment(models.Model):

    title = models.CharField(max_length=150)
    body = models.TextField()
    date_create = models.DateTimeField(auto_now_add=True, blank=True)
    date_modify = models.DateTimeField(auto_now=True, blank=True)
    # comment = GenericRelation("Comment")
    post = models.ForeignKey('Post', on_delete=models.CASCADE)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')
    auther = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    like = models.ManyToManyField(
        UserProfile, related_name="comment_likes", blank=True)
    dislike = models.ManyToManyField(
        UserProfile, related_name='comment_dislikes', blank=True)

    def __str__(self):
        return self.body[:20]

    def get_absolute_url(self):
        return reverse("post", kwargs={"post_slug": self.post.slug})+f"#{self.pk}"


class Post(models.Model):

    auth = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    slug = models.SlugField(max_length=200, blank=True)
    create_date = models.DateTimeField(auto_now_add=True, null=True)
    modify_date = models.DateTimeField(auto_now=True, null=True)
    title = models.CharField(max_length=150)
    body = models.TextField()
    date = models.DateField(auto_now_add=True)
    like = models.ManyToManyField(UserProfile, related_name="post_like")
    dislike = models.ManyToManyField(
        UserProfile, related_name="post_dislike", blank=True)
    # comment = models.ForeignKey(
    #     Comment, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        s = "author : {}" + " | " + "title : {}"
        return s.format(self.auth, self.title)

    def save(self, *args, **kwargs):
        if not self.slug:
            slug = f"{self.auth.user_id}-{slugify(self.title)}"
            self.slug = slug
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("post", kwargs={"slug": self.slug})

    def get_like_count(self):
        return self.like.count()

    def get_dislike_count(self):
        return self.dislike.count()


# class Likes(models.Model):
#     user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
#     post = models.ForeignKey(Post, on_delete=models.CASCADE)
#     value = models.BooleanField(default=False)
#     # date_create = models.DateTimeField(auto_now_add=True, blank=True)
#     # date_modify = models.DateTimeField(auto_now=True, blank=True)
#     # content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
#     # object_id = models.PositiveIntegerField()
#     # content_object = GenericForeignKey('content_type', 'object_id')

#     class Meta:
#         unique_together = ('user', 'post')

#     def __str__(self):
#         return str(self.post)

# class dislikes(models.Model):
#     user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
#     post = models.ForeignKey(Post, on_delete=models.CASCADE)
#     date_create = models.DateTimeField(auto_now_add=True, blank=True)
#     date_modify = models.DateTimeField(auto_now=True, blank=True)
#     like = models.BooleanField(default=False)
#     dislike = models.BooleanField(default=True)
#     content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
#     object_id = models.PositiveIntegerField()
#     content_object = GenericForeignKey('content_type', 'object_id')
#     class Meta:
#         unique_together = ('user', 'post')
#     def __str__(self):
#         return self.user.username

# class CommentLike(models.Model):
#     user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
#     comment = models.ForeignKey(Comment, on_delete=models.CASCADE)
#     date_create = models.DateTimeField(auto_now_add=True, blank=True)
#     date_modify = models.DateTimeField(auto_now=True, blank=True)
#     like = models.BooleanField(default=True)
#     dislike = models.BooleanField(default=False)
#     content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
#     object_id = models.PositiveIntegerField()
#     content_object = GenericForeignKey('content_type', 'object_id')
#     class Meta:
#         unique_together = ('user', 'comment')
#     def __str__(self):
#         return self.user.username

# class CommentDislike(models.Model):
    # user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    # comment = models.ForeignKey(Comment, on_delete=models.CASCADE)
    # date_create = models.DateTimeField(auto_now_add=True, blank=True)
    # date_modify = models.DateTimeField(auto_now=True, blank=True)
    # like = models.BooleanField(default=False)
    # dislike = models.BooleanField(default=True)
    # content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    # object_id = models.PositiveIntegerField()
    # content_object = GenericForeignKey('content_type', 'object_id')
    # class Meta:
    #     unique_together = ('user', 'comment')
    # def __str__(self):
    #     return self.user.username
