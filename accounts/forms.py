from django.forms import ModelForm
from .models import Profile
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = ['email']
        
        widgets = {
            'email':forms.TextInput(attrs={'class':'form-control is-invalid', 'id': 'validationTextarea','placeholder': 'Введите ваш e-mail...'}),
            
        }

class CreateUserForm(UserCreationForm):
    password1 = forms.CharField(widget = forms.PasswordInput(attrs = {'placeholder': 'Пароль...'}))
    password2 = forms.CharField(widget = forms.PasswordInput(attrs = {'placeholder': 'Подтвердите пароль...'}))
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        
        widgets = {
            'username': forms.TextInput(attrs={"placeholder": 'Имя пользователя...'}),
            'email': forms.TextInput(attrs={"placeholder": 'example@gmail.com'}),
            'password1': forms.PasswordInput(attrs={"placeholder": 'Введите пароль...'}),
            'password2': forms.PasswordInput(attrs={"placeholder": 'Подтвердите пароль...'})

        }

