from django.urls import path
from .views import (
    MessageListView,
    MessageDetailView,
    MessageCreateView,
    MessageUpdateView,
    MessageDeleteView,
)

app_name = 'user_messages'

urlpatterns = [
    path('', MessageListView.as_view(), name='message_list'),
    path('<int:pk>/', MessageDetailView.as_view(), name='message_detail'),
    path('create/', MessageCreateView.as_view(), name='message_create'),
    path('update/<int:pk>/', MessageUpdateView.as_view(), name='message_update'),
    path('delete/<int:pk>/', MessageDeleteView.as_view(), name='message_delete'),
]



