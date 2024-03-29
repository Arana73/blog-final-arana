from django import forms
from .models import Blog

class BlogPostForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['title', 'subtitle', 'body', 'image']
        labels = {
            'title': 'Título',
            'subtitle': 'Subtítulo',
            'body': 'Descripcion',
            'image': 'Imagen',
            }
