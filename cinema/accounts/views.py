from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.core.mail import send_mail
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import FormView
from accounts.forms import CreateUserForm
from accounts.models import Profile
from django.contrib.auth.models import User
import random as rand


def register(request):
    if request.user.is_authenticated:
        return redirect('home:home')
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            email = request.POST.get('email')
            all_users = User.objects.all()
            for i in all_users:
                if i.email == email:
                    unique_email = False
                else:
                    username = form.cleaned_data.get('username')
                    messages.success(request, 'Аккаунт был создан для ' + username + '. Проверьте вашу почту!')
                    user = form.save()
                    key = rand.randint(100000, 999999)
                    profile = Profile.objects.create(user=user, email=form.cleaned_data.get('email'), key=key)
                    user.email = profile.email
                    user.save()
                    user.is_active = False
                    user.save()
                    send_mail('Мы благодарим Вас за регистрацию на OK Online Cinema!', 'Код подтверждения: ' + str(key),
                              'arklual@gmail.com', [form.cleaned_data.get('email')],
                              fail_silently=False)
                    context = {'user': user}
                    return redirect('account:validate', user.id)
    form = CreateUserForm()
    context = {'form': form}
    return render(request, 'registration/signup.html', context)


def get_profile(request, id):
    prof = get_object_or_404(Profile, user_id=id)
    context = {
        "profile": prof,
    }
    return render(request, template_name="profile/profile.html", context=context)


def profile_settings(request, id):
    profile = get_object_or_404(Profile, user_id=id)
    context = {
        "profile": profile,
    }
    return render(request, template_name="profile/settings.html", context=context)


def upload_ava(request, id):
    profile = get_object_or_404(Profile, user_id=id)
    if request.method == 'POST':
        profile.image = request.FILES.get('ava')
        profile.save()
    context = {
        "profile": profile,
    }
    return render(request, template_name="profile/settings.html", context=context)


def change_email(request, id):
    profile = get_object_or_404(Profile, user_id=id)
    if request.method == 'POST':
        profile.email = request.POST.get('email')
        profile.save()
        profile.user.email = request.POST.get('email')
        profile.user.save()
    context = {
        "profile": profile,
    }
    return render(request, template_name="profile/settings.html", context=context)


def change_name(request, id):
    profile = get_object_or_404(Profile, user_id=id)
    if request.method == 'POST':
        profile.user.username = request.POST.get('name')
        profile.user.save()
    context = {
        "profile": profile,
    }
    return render(request, template_name="profile/settings.html", context=context)


def validate(request, id):
    user = get_object_or_404(User, id=id)
    context = {
            "us": user,
    }
    profile = get_object_or_404(Profile, user=user)
    if user.is_active:
        login(request, user)
        return redirect('account:profile', user.id)
    else:
        if request.method == 'POST':
            key = request.POST.get('key')
            if str(profile.key) == key:
                user.is_active = True
                login(request, user)
                return redirect('home:home')
    return render(request, 'registration/validate.html', context=context)
