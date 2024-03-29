# accounts/forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile
from django.contrib.auth.forms import AuthenticationForm



class LoginForm(AuthenticationForm):
    pass
               

class SignUpForm(UserCreationForm):
    email = forms.EmailField(label='Email', max_length=254)
    username = forms.CharField(label='Nombre de usuario', max_length=150)
    password1 = forms.CharField(label='Contraseña', max_length=254, widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirmar Contraseña', max_length=254, widget=forms.PasswordInput)

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





