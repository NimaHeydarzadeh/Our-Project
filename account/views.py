from django.contrib import messages
from django.contrib.auth import login
from forms.SignUpForm import NewUserForm
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from forms.Forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm




# Create your views here.


def login(request):

    return render(request, 'account/login.html', context={})


def signup(request):

    if request.method == "POST":
        form=NewUserForm(request.POST)
        if form.is_valid():
            user =form.save()
            # login(request, user)
            messages.success(request, "Registration successful.")
            return redirect("home")
        messages.error(request, "Unsuccessful registration. Invalid information.")
    form = NewUserForm()
    return render (request=request, template_name="account/signup.html", context={"register_form":form})


@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST,
                                   request.FILES,
                                   instance=request.user.userprofile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('profile')  # Redirect back to profile page

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.userprofile)

    context = {
        'u_form': u_form,
        'p_form': p_form
    }

    return render(request, 'account/profile.html', context)
