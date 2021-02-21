from django.shortcuts import render
from films.models import Film
from serials.models import Serial, Seriya
from itertools import chain

def dateMovieList(request):
    filmList = Film.objects.order_by('-date')
    serialList = Serial.objects.order_by('-date')
    movieList = sorted(chain(filmList, serialList), key=lambda instance: instance.date)
    context = {}
    context['movieList'] = movieList
    return render(request, "partial/list.html", context)
