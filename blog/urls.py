from django.urls import include, path
from blog import views


class developer_urls:
    urlpatterns = [
        path('Farid/', views.developer, name='Farid'),
        path('Nima/', views.developer, name='Nima'),
    ]

urlpatterns = [
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    # path('developer/<str:developer_name>', views.developer, name='developer'),
    path('developer/',include(developer_urls)),
    path('home/', views.home, name='home'),
    path('index/', views.home, name='index'),
    path('post/<slug:slug>', views.post, name='post'),
    path('posts/', views.posts, name='posts'),
    # path('posts/like/', views.like_posts, name='like_posts'),
    # path('posts/dislike/', views.dislike_posts, name='dislike_posts'),
]



