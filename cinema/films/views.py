from django.shortcuts import render, get_object_or_404, Http404
from films.models import Film
from marks.forms import BallForm
from marks.models import Voter

def single(request, id=None):
    form = BallForm
    film = get_object_or_404(Film, id=id)
    context = {
        "notIsMarked": not Voter.objects.filter(film_id=id, user_id=request.user.id).exists(),
        "film": film,
        "form": form,
    }
    return render(request, "partial/single.html", context)
