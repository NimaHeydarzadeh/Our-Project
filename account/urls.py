from django.shortcuts import redirect
from django.urls import include, path
from account import views
from django.contrib.auth.views import LoginView
from forms.UserLoginForm import UserLoginForm




urlpatterns = [
    # path('login/', views.login, name='login'),
    path('signup/', views.signup, name='signup'),
    # path("accounts/", include("django.contrib.auth.urls")),
    path('login/', LoginView.as_view(
        template_name="account/login.html",
        authentication_form=UserLoginForm
    ), name="login"),
    path('profile/', views.profile, name='profile'),
    path('logout/', views.logout_view, name='logout'),
    
]
