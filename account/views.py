from django.shortcuts import render

# Create your views here.


def login(request):
    return render(request, 'account/login.html', context={})


def signup(request):
    return render(request, 'account/signup.html', context={})


