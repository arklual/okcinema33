from django.shortcuts import render, get_object_or_404, Http404
from films.models import Film, Seriya
def player(request, id=None, season=None, number=None):
    try:
        video = get_object_or_404(Film, id=id)
    except Http404:
        video = get_object_or_404(Seriya, season=season, number=number) 
    context={
        "v":video,
    }
    return render(request, "partial/player.html", context)