from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class BallForm(forms.Form):
    ball = forms.IntegerField(min_value=1, max_value=10, label="Оценка")
