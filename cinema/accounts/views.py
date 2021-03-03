from django.shortcuts import render, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import FormView
from accounts.forms import CreateUserForm
from accounts.models import Profile
from django.contrib.auth.models import User

class MyRegisterFormView(FormView):
    form_class = CreateUserForm
    success_url = reverse_lazy('login')
    template_name = "registration/signup.html"

    def form_valid(self, form):
        form.save()
        return super(MyRegisterFormView, self).form_valid(form)
    def form_invalid(self, form):
        return super(MyRegisterFormView, self).form_invalid(form)

def get_profile(request, username):
    us = get_object_or_404(User, username=username)
    prof = get_object_or_404(Profile, user=us)
    context = {
        "profile":prof,
    }
    return render(request, template_name="profile/profile.html", context=context)
