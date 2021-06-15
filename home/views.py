from django.shortcuts import render, get_object_or_404, Http404
from films.models import Film
from serials.models import Serial
from itertools import chain

def home(request):
    filmList = Film.objects.order_by('-date')
    list1 = list(chain(filmList))
    while len(list1) > 3:
        del list1[len(list1)-1]
    serialList = Serial.objects.order_by('-date')
    list2 = list(chain(serialList))
    while len(list2) > 3:
        del list2[len(list2)-1]
    context = {
        "filmList": list1,
        "sList": list2,
        "title": "Главная страница кинотеатра",
    }
    return render(request, "partial/home.html", context)