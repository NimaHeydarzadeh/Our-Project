from django.db.models.signals import post_save  # Import a post_save signal when a user is created
from .models import Profile
from django.dispatch import receiver # Import the receiver
from django.contrib.auth.models import User # Import the built-in User model, which is a sender
from django.dispatch import receiver
from django.db.models.signals import pre_save, post_save

from models import User, UserProfile


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()
