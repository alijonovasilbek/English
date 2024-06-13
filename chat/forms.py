from django import forms
from .models import Message, Room

class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ['content', 'image']

class RoomForm(forms.ModelForm):
    class Meta:
        model = Room
        fields = ['name']
