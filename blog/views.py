from multiprocessing import AuthenticationError
from django.http import Http404
from django.shortcuts import get_object_or_404, redirect, render
from django.db import models
from .models import UserProfile, Post, Comment
from django.db.models import Count, Prefetch, F
from django.contrib.auth.decorators import login_required


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
        if request.method == "POST":
            p = Comment(author=request.user.userprofile,
                        content_object=Post.objects.get(slug=slug),
                        body=request.POST['text'])
            p.save()
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
    except Post.DoesNotExist:
        raise Http404("Post does not exist")

    return render(request, 'blog/post.html', context={"post": post, "comments": comments})


def posts(request):
    if request.method == "GET":
        posts = Post.objects.all().annotate(username=models.F('author__user__username'))
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
