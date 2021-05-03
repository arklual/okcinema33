from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from ckeditor.widgets import CKEditorWidget

class BallForm(forms.Form):
    ball = forms.IntegerField(min_value=1, max_value=10, label="Оценка")

class ResensionForm(forms.Form):
    title = forms.CharField(max_length=120, label='Название рецензии')
    text = forms.CharField(widget=CKEditorWidget, label='Текст рецензии')
