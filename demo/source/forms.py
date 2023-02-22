from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from .models import Course, Topic, Student


class LoginForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ['username', 'password']
