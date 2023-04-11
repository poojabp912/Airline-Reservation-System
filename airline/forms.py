from django.contrib.auth.forms import UserCreationForm
# from django import forms
from django.contrib.auth.models import User

class CreateUs(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','password','email']