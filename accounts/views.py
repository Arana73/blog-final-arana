from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView
from .forms import SignUpForm, LoginForm, UserUpdateForm, ProfileUpdateForm
from .models import Profile
from django.contrib.auth.forms import AuthenticationForm
from django.views.generic import FormView
from django.http import HttpResponseRedirect


# Vista para registrar nuevos usuarios
class SignUpView(CreateView):
    template_name = 'accounts/signup.html'
    form_class = SignUpForm
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return super().form_valid(form)


# Vista para iniciar sesión
class LoginView(FormView):
    template_name = 'accounts/login.html'
    form_class = AuthenticationForm
    success_url = reverse_lazy('home')  

    def form_valid(self, form):
        user = form.get_user()
        login(self.request, user)
        return super().form_valid(form)


# Vista para ver el perfil de usuario
class ProfileDetailView(DetailView):
    model = Profile
    template_name = 'accounts/profile.html'
    context_object_name = 'profile'
    

# Vista para actualizar el perfil de usuario
class ProfileUpdateView(UpdateView):
    model = Profile
    form_class = ProfileUpdateForm
    template_name = 'accounts/edit_profile.html'

    def get_success_url(self):
        return reverse_lazy('accounts:profile', kwargs={'pk': self.object.pk})

# Vista para cerrar sesión
@login_required
def logout_view(request):
    logout(request)
    return redirect('home')


