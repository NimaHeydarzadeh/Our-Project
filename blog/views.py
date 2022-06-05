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

    return render(request, 'blog/About.html', context={})


def contact(request):
    return render(request, 'blog/Contact.html', context={})


def developer(request):
    developer_name = resolve(request.path_info).url_name
    return render(request, 'blog/Developer.html', context={"developer_name": developer_name})


def home(request):
    return render(request, 'blog/Home.html', context={})


def index(request):
    return render(request, 'blog/index.html', context={})


# def post(request,post):
#     post = get_object_or_404(Post, slug=post)

#     # List of active comments for this post
#     comments = post.comments.filter(active=True)

#     new_comment = None

#     if request.method == 'POST':
#         # A comment was posted
#         comment_form = CommentForm(data=request.POST)
#         if comment_form.is_valid():
#             # Create Comment object but don't save to database yet
#             new_comment = comment_form.save(commit=False)
#             # Assign the current post to the comment
#             new_comment.post = post
#             # Save the comment to the database
#             new_comment.save()
#     else:
#         comment_form = CommentForm()
#     return render(request,
#                   'blog/post.html',
#                   {'post': post,
#                    'comments': comments,
#                    'new_comment': new_comment,
#                    'comment_form': comment_form})

def post(request, slug):

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
        # like_num = request.POST.get('like_num')
        # dislike_num = request.POST.get('dislike_num')
        # likes = Post(author=UserProfile.objects.get(pk=2),
        #              like=like_num, dislike=dislike_num, post=post, content_object=post)
        # likes.save()
    except Post.DoesNotExist:
        raise Http404("Post does not exist")

    return render(request, 'blog/post.html', context={"post": post, "comments": comments, "comment_saved": comment_saved})



def posts(request):

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
        return render(request, 'blog/posts.html', context={"posts": posts, "post_saved": post_saved})
    posts1 = Post.objects.all()
    return render(request, 'blog/Posts.html', context={"posts1": posts1})


def Messages(request):

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

        return render(request, 'blog/posts.html', context={"message_saved": message_saved})


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
