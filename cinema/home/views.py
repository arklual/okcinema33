from django.shortcuts import render, get_object_or_404, Http404
from films.models import Film
from serials.models import Serial

def home(request):
    filmList = Film.objects.order_by('-date')
    while filmList.count() > 3:
        del filmList[filmList.count-1]
    serialList = Serial.objects.order_by('-date')
    while serialList.count() > 3:
        del serialList[serialList.count-1]
    context = {
        "filmList": filmList,
        "sList": serialList,
        "title": "Главная страница кинотеатра",
    }
    return render(request, "partial/home.html", context)