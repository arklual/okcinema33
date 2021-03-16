from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SearchForm(forms.Form):
    search_request = forms.CharField(max_length=120, widget = forms.TextInput(attrs = {'placeholder': 'Поиск'}))
