from django import forms
from .models import Comment


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content', 'parent']
        widgets = {
            'content': forms.Textarea(attrs={'rows': 4, 'placeholder': 'Leave a comment...'}),
            'parent': forms.HiddenInput(),
        }
