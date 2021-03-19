from django.shortcuts import render, Http404
from serials.models import Serial
from films.models import Film
from search.forms import SearchForm


def search(request):
    search_request = request.GET.get('request')
    try:
        movieList = Film.objects.filter(title__contains=search_request)
    except Http404:
        movieList = Serial.objects.filter(title__contains=search_request)
    context = {
       'movieList': movieList,
    }
    return render(request, "partial/list.html", context)