from django.urls import path
from blog import views


urlpatterns = [
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('developer/', views.contact, name='developer'),
    path('home/', views.home, name='home'),
    path('post/', views.post, name='post'),
    path('posts/', views.posts, name='posts'),
]
