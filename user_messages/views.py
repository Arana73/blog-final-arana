# En el archivo views.py de la app user_messages

from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Message
from .forms import MessageForm

class MessageListView(ListView):
    model = Message
    template_name = 'messages/message_list.html'
    context_object_name = 'messages'

class MessageDetailView(DetailView):
    model = Message
    template_name = 'messages/message_detail.html'
    context_object_name = 'message'

class MessageCreateView(CreateView):
    model = Message
    form_class = MessageForm
    template_name = 'messages/message_form.html'
    success_url = reverse_lazy('user_messages:message_list')
    
    def form_valid(self, form):
        form.instance.sender = self.request.user
        return super().form_valid(form)

class MessageUpdateView(UpdateView):
    model = Message
    fields = ['receiver', 'subject', 'body']
    template_name = 'messages/message_form.html'
    success_url = reverse_lazy('message_list')

class MessageDeleteView(DeleteView):
    model = Message
    template_name = 'messages/message_confirm_delete.html'
    success_url = reverse_lazy('user_messages:message_list')

