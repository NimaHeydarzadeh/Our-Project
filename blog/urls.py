from django.urls import path
from blog import views

urlpatterns = [
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('developer/', views.developer, name='developer'),
    path('home/', views.home, name='home'),
    path('index/', views.home, name='index'),
    path('post/', views.post, name='post'),
    path('posts/', views.posts, name='posts'),
    # path('posts/like/', views.like_posts, name='like_posts'),
    # path('posts/dislike/', views.dislike_posts, name='dislike_posts'),
]

