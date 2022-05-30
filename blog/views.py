from multiprocessing import AuthenticationError
from django.shortcuts import redirect, render
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


def post(request, slug):

    if request.method == "GET":
        posts = Post.objects.filter(slug=slug)
        # print(posts)
        # print(posts.query)
        return render(request, 'blog/post.html', context={"post": posts})
    elif request.method == "POST":
        print(request.POST.get('comment_body'))
        return render(request, 'blog/post.html', context={"post": posts})


def posts(request):
    if request.method == "GET":
        posts = Post.objects.all().annotate(username=models.F('auth__user__username'))
        # print(posts)
        # print(posts.query)
        return render(request, 'blog/posts.html', context={"posts": posts})
    posts1 = Post.objects.all()
    return render(request, 'blog/Posts.html', context={posts1: posts1})

# def like_posts(request):
#     if request.method == "GET":
#         pass
#     elif request.method == "POST":
#         pass
#     return redirect('blog/posts.html:posts')


# def dislike_posts(request):
#     if request.method == "GET":
#         pass
#     elif request.method == "POST":
#         pass
#     return redirect('blog/posts.html:posts')
