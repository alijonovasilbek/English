from django import forms
from app_pages.models import Category
from django import forms
from ckeditor.widgets import CKEditorWidget
from app_pages.models import Dars


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['course_name']


class DarsForm(forms.ModelForm):
    video_url = forms.CharField(widget=CKEditorWidget())
    text = forms.CharField(widget=CKEditorWidget())

    class Meta:
        model = Dars
        fields = ['number', 'name', 'video_url', 'description', 'text', 'file', 'category']
