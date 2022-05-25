from django.shortcuts import render
from django.db import models
# from .models import Post, UserProfile
# Create your views here.


def home(request):
    return render(request, 'blog/Home.html', context={})


def post(request):
    return render(request, 'blog/Post.html', context={})


def posts(request):
    return render(request, 'blog/Posts.html', context={})


def about(request):
    return render(request, 'blog/about.html', context={})
