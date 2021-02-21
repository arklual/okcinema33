from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, Http404
from films.models import Film
from serials.models import Serial
from marks.forms import BallForm
from marks.models import Voter

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
def single(request, id=None):
    form = BallForm
    film = get_object_or_404(Film, id=id)
    context = {
        "notIsMarked": not Voter.objects.filter(film_id=id, user_id=request.user.id).exists(),
        "film": film,
        "form": form,
    }
    return render(request, "partial/single.html", context)
