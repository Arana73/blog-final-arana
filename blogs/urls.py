from django.urls import path
from .views import (
    BlogListView,
    BlogDetailView,
    BlogCreateView,
    BlogUpdateView,
    BlogDeleteView,
)

app_name = 'blogs'

urlpatterns = [
    path('', BlogListView.as_view(), name='blogs'),
    path('blog/<int:pk>/', BlogDetailView.as_view(), name='blog_detail'),
    path('create/', BlogCreateView.as_view(), name='create_blog'),
    path('update/<int:pk>/', BlogUpdateView.as_view(), name='update_blog'),
    path('delete/<int:pk>/', BlogDeleteView.as_view(), name='delete_blog'),

]


