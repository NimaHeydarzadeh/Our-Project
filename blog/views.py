from django.shortcuts import render
from django.db import models
from .models import UserProfile, Post
# from .models import Post, UserProfile
# Create your views here.


def home(request):
    return render(request, 'blog/Home.html', context={})


def post(request):
    # post1 = Post.objects.filter().values('title', 'body', 'like', 'dislike')
    return render(request, 'blog/Post.html', context={})


def posts(request):
    posts1 = Post.objects.all()
    return render(request, 'blog/Posts.html', context={posts1: posts1})


def about(request):
    return render(request, 'blog/about.html', context={})
