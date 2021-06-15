from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, Http404
from films.models import Film
from serials.models import Serial, Seriya
from marks.models import Voter, SerialVoter, FilmRecension, SerialRecension
from .forms import BallForm, ResensionForm
from accounts.models import Profile

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
            profile = get_object_or_404(Profile, user_id=request.user.id)
            profile.numberOfMarks += 1
            profile.reputation += 1
            profile.save()
            v.save()
        except Http404:
            film = get_object_or_404(Serial, id=id)
            if SerialVoter.objects.filter(serial_id=id, user_id=request.user.id).exists():
                context = {
                    "text": "Вы уже оценили этот сериал",
                    "title": "Ошибка",
                }
                return render(request, "partial/information.html", context)
            v=SerialVoter(user=request.user, serial=film)
            v.save()
        b = form.cleaned_data['ball']
        film.raiting = round((film.raiting * film.numMarks + b)/(film.numMarks+1), 1)
        film.numMarks+=1
        profile.reputation += 1
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
def recension(request, id=id):
    rForm = ResensionForm(request.POST)
    form = BallForm(request.POST)
    if rForm.is_valid():
        title = rForm.cleaned_data['title']
        text = rForm.cleaned_data['text']
        try:
            film = get_object_or_404(Film, id=id)
            if FilmRecension.objects.filter(film_id=id, user_id=request.user.id).exists():
                context = {
                    "text": "Вы уже написали рецензию на этот фильм",
                    "title": "Ошибка",
                }
                return render(request, "partial/information.html", context)
            r=FilmRecension(user=request.user, film=film, title=title, text=text)
            profile = get_object_or_404(Profile, user_id=request.user.id)
            profile.numberOfRecensions += 1
            profile.reputation += 100
            profile.save()
            r.save()
        except Http404:
            film = get_object_or_404(Serial, id=id)
            if SerialRecension.objects.filter(serial_id=id, user_id=request.user.id).exists():
                context = {
                    "text": "Вы уже написали рецензию на этот сериал",
                    "title": "Ошибка",
                }
                return render(request, "partial/information.html", context)
            r=SerialRecension(user=request.user, serial=film, title=title, text=text)
            profile.numberOfRecensions += 1
            profile.reputation += 100
            r.save()
        if type(film)==Film:
            recension_list = FilmRecension.objects.filter(film=film)
        elif type(film)==Serial:
            recension_list = SerialRecension.objects.filter(serial=film)
        context = {
        "rList":recension_list,
        "film": film,
        }
        return render(request, "partial/recension_list.html", context)
    else:
        try:
            f = get_object_or_404(Film, id=id)
        except Http404:
            f = get_object_or_404(Serial, id=id)
        context = {
            "rForm": rForm,
            "film": f,
        }
        return render(request, "partial/createRecension.html", context)
def recension_list(request, id=id):
    try:
        f = get_object_or_404(Film, id=id)
        recension_list = FilmRecension.objects.filter(film=f)
    except Http404:
        f = get_object_or_404(Serial, id=id)
        recension_list = SerialRecension.objects.filter(serial=f)
    context = {
        "rList":recension_list,
        "film": f,
    }
    return render(request, "partial/recension_list.html", context)
def single_recension(request, id=id):
    try:
        recension = get_object_or_404(FilmRecension, id=id)
    except Http404:
        recension = get_object_or_404(SerialRecension, id=id)
    context = {
        "r": recension,
    }
    return render(request, "partial/single_recension.html", context)
def info(request):
    context = {
        "text": "Здесь должна быть информация",
        "title": "Информация",
    }
    return render(request, "partial/information.html", context)