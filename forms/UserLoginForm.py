from django.contrib.auth.forms import AuthenticationForm, UsernameField

from django import forms


class UserLoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(UserLoginForm, self).__init__(*args, **kwargs)

    username = UsernameField(widget=forms.TextInput(
        attrs={'class': 'u-grey-5 u-input u-input-rectangle u-radius-25 u-input-1', 'placeholder': 'Enter your Username', 'id': 'username-a30d'}))
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={
            'class': 'u-grey-5 u-input u-input-rectangle u-radius-25 u-input-2',
            'placeholder': 'Enter your Password',
            'id': 'password-a30d',
        }
    ))
