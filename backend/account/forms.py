from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User

class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['email', 'name', 'password1', 'password2']


class EditProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['name', 'email', 'avatar']
        
    