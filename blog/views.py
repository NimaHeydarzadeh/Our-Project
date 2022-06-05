from multiprocessing import AuthenticationError
from nturl2path import url2pathname
from unicodedata import name
from wsgiref.util import request_uri
from django.http import Http404
from django.shortcuts import get_object_or_404, redirect, render
from django.db import models
from django.urls import get_urlconf
from .models import UserProfile, Post, Comment
from django.db.models import Count, Prefetch, F
from django.contrib.auth.decorators import login_required
from django.urls import resolve


# Create your views here.


# def about(request):
#     return render(request, 'blog/About.html', context={})


# def contact(request):
#     return render(request, 'blog/Contact.html', context={})


# def developer(request):
#     return render(request, 'blog/Developer.html', context={})


# def home(request):
#     return render(request, 'blog/Home.html', context={})


# def index(request):
#     return render(request, 'blog/index.html', context={})


# def post(request, slug):
#     try:
#         if request.method == "POST":
#             p = Comment(author=request.user.userprofile,
#                         content_object=Post.objects.get(slug=slug),
#                         body=request.POST['text'])
#             p.save()
#             print(posts)
#             print(posts.query)
#         post = (Post.objects.prefetch_related(
#             Prefetch('comment',
#                      queryset=(Comment.objects
#                                .annotate(username=F('author__user__username'))
#                                .select_related('author')
#                                .annotate(like_count=Count('like'))
#                                .annotate(dislike_count=Count('dislike'))
#                                )
#                      )
#         )
#             .annotate(like_count=Count('like'))
#             .annotate(dislike_count=Count('dislike'))
#             .annotate(comments_count=Count('comment'))
#             .annotate(username=F('author__user__username'))
#             .select_related('author')
#             .get(slug=slug)
#         )
#     except Post.DoesNotExist:
#         raise Http404("Post does not exist")

#     return render(request, 'blog/post.html', context={"post": post})

##############################################################################################
def about(request):
    if request.user.is_authenticated:
        is_authenticated = True
    else:
        is_authenticated = False
    return render(request, 'blog/About.html', context={"is_authenticated":is_authenticated})


def contact(request):
    if request.user.is_authenticated:
        is_authenticated = True
    else:
        is_authenticated = False
    return render(request, 'blog/Contact.html', context={"is_authenticated": is_authenticated})


def developer(request):
    if request.user.is_authenticated:
        is_authenticated = True
    else:
        is_authenticated = False
    developer_name = resolve(request.path_info).url_name
    return render(request, 'blog/Developer.html', context={"developer_name": developer_name, "is_authenticated": is_authenticated})


def home(request):
    if request.user.is_authenticated:
        is_authenticated = True
    else:
        is_authenticated = False
    return render(request, 'blog/Home.html', context={"is_authenticated": is_authenticated})


def post(request, slug):

    if request.user.is_authenticated:
        is_authenticated = True
    else:
        is_authenticated = False

    try:
        comment_saved = True
        if request.method == "POST":

            new_comment = Comment(author=request.user.userprofile,
                                  content_type_id=7, object_id=10,
                                  post_id=Post.objects.get(slug=slug).id,
                                  body=request.POST['comment_body'],
                                  title=request.POST['comment_title'])
            try:
                new_comment.save()
                comment_saved = True
            except:
                comment_saved = False

        post = (Post.objects.prefetch_related(
            Prefetch('comment',
                     queryset=(Comment.objects
                               .annotate(username=F('author__user__username'))
                               .select_related('author')
                               .annotate(like_count=Count('like'))
                               .annotate(dislike_count=Count('dislike'))
                               )
                     )
        )
            .annotate(like_count=Count('like'))
            .annotate(dislike_count=Count('dislike'))
            .annotate(comments_count=Count('comment'))
            .annotate(username=F('author__user__username'))
            .select_related('author')
            .get(slug=slug)
        )
        comments = post.comments.all()
        # likes = Post(author=UserProfile.objects.get(pk=2),
        #              like=like_num, dislike=dislike_num, post=post, content_object=post)
        # likes.save()
    except Post.DoesNotExist:
        raise Http404("Post does not exist")

    return render(request, 'blog/post.html', context={"post": post, "comments": comments, "comment_saved": comment_saved, "is_authenticated": is_authenticated})



def posts(request):

    if request.user.is_authenticated:
        is_authenticated = True
    else:
        is_authenticated = False

    post_saved = True
    if request.method == "POST":
        new_post = Post(author=request.user.userprofile,
                        body=request.POST['post_body'],
                        title=request.POST['post_title'])
        try:
            new_post.save()
            post_saved = True
        except:
            post_saved = False

    elif request.method == "GET":
        posts = Post.objects.all().annotate(username=models.F('author__user__username'))
        # print(posts)
        # print(posts.query)
        return render(request, 'blog/posts.html', context={"posts": posts, "post_saved": post_saved, "is_authenticated": is_authenticated})
    posts1 = Post.objects.all()
    return render(request, 'blog/Posts.html', context={"posts1": posts1, "is_authenticated": is_authenticated})


def Messages(request):

    if request.user.is_authenticated:
        is_authenticated = True
    else:
        is_authenticated = False

    message_saved = True
    if request.method == "POST":
        new_message = Messages(name=request.POST['name'],
                               messege=request.POST['message'],
                               email=request.POST['email'])
        try:
            new_message.save()
            message_saved = True
        except:
            message_saved = False

        return render(request, 'blog/posts.html', context={"message_saved": message_saved, "is_authenticated": is_authenticated})


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
