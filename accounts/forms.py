# accounts/forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile
from django.contrib.auth.forms import AuthenticationForm
from .models import BlogPost


class LoginForm(AuthenticationForm):
    pass
               

class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=254, help_text='')

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')



class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']
        
        


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['nombre', 'descripcion', 'imagen']  





class BlogPostForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ['title', 'subtitle', 'body', 'image']
