from django.shortcuts import render
from django.db import models
from .models import UserProfile, Post
# from .models import Post, UserProfile
# Create your views here.


def about(request):
    return render(request, 'blog/About.html', context={})


def contact(request):
    return render(request, 'blog/Contact.html', context={})


def developer(request):
    return render(request, 'blog/Developer.html', context={})


def home(request):
    return render(request, 'blog/Home.html', context={})


def index(request):
    return render(request, 'blog/index.html', context={})


def post(request):
    # post1 = Post.objects.filter().values('title', 'body', 'like', 'dislike')
    return render(request, 'blog/Post.html', context={})


def posts(request):
    posts1 = Post.objects.all()
    return render(request, 'blog/Posts.html', context={posts1: posts1})
