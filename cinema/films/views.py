from django.http import HttpResponse
from django.views.generic.edit import FormView
from django.shortcuts import render, get_object_or_404, Http404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.forms import UserCreationForm

from films.models import Film, Serial, Seriya, Voter, SerialVoter
from .forms import BallForm

def home(request):
    filmList = Film.objects.order_by('-date')
    serialList = Serial.objects.order_by('-date')
    context = {
        "filmList": filmList,
        "sList": serialList,
        "title": "Главная страница кинотеатра",
    }
    return render(request, "partial/home.html", context)
def single(request, id=None):
    form = BallForm
    try:
        film = get_object_or_404(Film, id=id)
    except Http404:
        film = get_object_or_404(Serial, id=id)
    context = {
        "notIsMarked": not Voter.objects.filter(film_id=id, user_id=request.user.id).exists(),
        "film": film,
        "form": form,
    }
    return render(request, "partial/single.html", context)
def serial(request, id=None):
    form = BallForm
    serial = get_object_or_404(Serial, id=id)
    context = {
        "notSerIsMarked": not SerialVoter.objects.filter(serial_id=id, user_id=request.user.id).exists(),
        "s": serial,
        "range": range(serial.count_sesonov),
        "form": form,
    }
    context['sers'] = serial.seriya_set.all().filter()
    return render(request, "partial/single_serial.html", context)
def full_player(request, id=None, season=None, number=None):
    try:
        video = get_object_or_404(Film, id=id)
    except Http404:
        video = get_object_or_404(Seriya, season=season, number=number) 
    context={
        "v":video,
    }
    return render(request, "partial/player.html", context)
def ball(request, id=id):
    form = BallForm(request.POST)
    if form.is_valid():
        try:
            film = get_object_or_404(Film, id=id)
            if Voter.objects.filter(film_id=id, user_id=request.user.id).exists():
                context = {
                    "text": "Вы уже оценили этот фильм",
                    "title": "Ошибка",
                }
                return render(request, "partial/information.html", context)
            v=Voter(user=request.user, film=film)
            v.save()
        except Http404:
            film = get_object_or_404(Serial, id=id)
            if SerialVoter.objects.filter(serial_id=id, user_id=request.user.id).exists():
                context = {
                    "text": "Вы уже оценили этот фильм",
                    "title": "Ошибка",
                }
                return render(request, "partial/information.html", context)
            v=SerialVoter(user=request.user, serial=film)
            v.save()
        b = form.cleaned_data['ball']
        film.raiting = round((film.raiting * film.numMarks + b)/(film.numMarks+1), 1)
        film.numMarks+=1
        film.save()
        if type(film)==Film:
            context = {
                "notIsMarked": not Voter.objects.filter(film_id=id, user_id=request.user.id).exists(),
                "film": film,
                "form": form,
            }
            return render(request, "partial/single.html", context)
        elif type(film)==Serial:
            context = {
                "form": form,
                "notSerIsMarked": not SerialVoter.objects.filter(serial_id=id, user_id=request.user.id).exists(),
                "s": film,
                "range": range(film.count_sesonov),
            }
            return render(request, "partial/single_serial.html", context)
def info(request):
    context = {
        "text": "Здесь должна быть информация",
        "title": "Информация",
    }
    return render(request, "partial/information.html", context)