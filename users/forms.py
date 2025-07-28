# users/forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import CustomUser


class UserRegisterForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['email', 'password1', 'password2']


class UserLoginForm(AuthenticationForm):
    username = forms.EmailField(label='Email')  # Переопределяем под email
