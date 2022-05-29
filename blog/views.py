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

    if request.method == "GET":
        posts = Post.objects.all()
        print(posts)
        print(posts.query)
        return render(request, 'blog/post.html', context={"post":posts})
    elif request.method == "POST":
        pass
    


def posts(request):
    if request.method == "GET":
        posts = Post.objects.all()
        print(posts)
        print(posts.query)
        return render(request, 'blog/posts.html', context={"posts":posts})
    posts1 = Post.objects.all()
    return render(request, 'blog/Posts.html', context={posts1: posts1})
