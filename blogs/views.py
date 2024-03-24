from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from .models import Blog
from .forms import BlogPostForm
import logging

logger = logging.getLogger(__name__)

class BlogListView(ListView):
    model = Blog
    template_name = 'blogs/blogs.html'
    context_object_name = 'blogs'

class BlogDetailView(DetailView):
    model = Blog
    template_name = 'blogs/blog_detail.html'
    context_object_name = 'blog'



class BlogCreateView(LoginRequiredMixin, CreateView):
    model = Blog
    form_class = BlogPostForm
    template_name = 'blogs/create_blog.html'
    success_url = reverse_lazy('blogs:create_blog')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class BlogUpdateView(UpdateView):
    model = Blog
    form_class = BlogPostForm
    template_name = 'blogs/update_blog.html'

    def get_success_url(self):
        return reverse_lazy('blogs:blog_detail', kwargs={'pk': self.object.pk})

 

class BlogDeleteView(LoginRequiredMixin, DeleteView):
    model = Blog
    success_url = reverse_lazy('blogs:blogs')
    template_name = 'blogs/blog_confirm_delete.html'

