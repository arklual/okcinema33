from django.shortcuts import render, get_object_or_404, Http404
from films.models import Film, Genre
from marks.forms import BallForm
from marks.models import Voter
from lxml import etree
from urllib import request as rqs

def single(request, id=None):
    form = BallForm
    film = get_object_or_404(Film, id=id)
    kp_url = "https://rating.kinopoisk.ru/"+film.kp_id+".xml"
    kp_rait = 0
    imdb_rait = 0
    f_xml = rqs.urlopen(kp_url)
    xml = f_xml.read()
    xml_root = etree.fromstring(xml)
    for elem in xml_root.getchildren():
        if not elem.text:
            text = "None"
        else:
            text = elem.text
        if(elem.tag == "kp_rating"):
            kp_rait = float(elem.text)
        if(elem.tag == "imdb_rating"):
            imdb_rait = float(elem.text)

    genres = Genre.objects.filter(film_id = film.id)
    context = {
        "notIsMarked": not Voter.objects.filter(film_id=id, user_id=request.user.id).exists(),
        "film": film,
        "form": form,
        "genres": genres,
    }
    kp_exist = False
    imdb_exist = False
    context['kp_rait'] = kp_rait
    context['imdb_rait'] = imdb_rait
    if(not kp_rait == 0):
        kp_exist = True
    if(not imdb_rait == 0):
        imdb_exist = True
    context['kp_exist'] = kp_exist
    context['imdb_exist'] = imdb_exist
    return render(request, "partial/single.html", context)
