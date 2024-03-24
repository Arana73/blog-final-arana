# blogs/models.py
from django.db import models
from django.contrib.auth.models import User

class Blog(models.Model):
    title = models.CharField(max_length=100)
    subtitle = models.CharField(max_length=100)
    body = models.TextField()
    image = models.ImageField(upload_to='blog_images')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    pub_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
