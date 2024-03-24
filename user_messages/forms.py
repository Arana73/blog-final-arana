from django import forms
from .models import Message

class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ['receiver', 'subject', 'body']
        labels = {
            'receiver': 'Destinatario',
            'subject': 'Asunto',
            'body': 'Cuerpo del mensaje',
        }
