from django.http import JsonResponse
from django.shortcuts import render
from films.models import Film, Genre
from serials.models import Serial,Seriya

def film_list(request):
    films = Film.objects.all()
    movies = []
    for film in films:
        name = film.title
        thumb = film.poster.url
        video = film.video
        genres = Genre.objects.filter(film=film)
        genre = ''
        for i in genres:
            genre += (i.name+' ')
        movies.append({
            'name' : name,
            'thumb' : thumb,
            'video' : video,
            'genre' : genre
        })
    
    return JsonResponse(movies, safe=False)


def serial_list(request):
    serials = Serial.objects.all()
    serial_list = []
    for serial in serials:
        episods = Seriya.objects.filter(serial=serial)
        ser = {
            'serial': serial,
            'episods': episods
        }
        serial_list.append(ser)
    serials = []
    for serial in serial_list:
        name = serial['serial'].title
        thumb = serial['serial'].poster.url
        episods = serial['episods']
        episod_list = []
        for episod in episods:
            name = episod.title
            season_number = episod.season
            number = episod.number
            fullname = f'{season_number}.{number}. {name}'
            video = episod.video
            ep = {
                'name': fullname,
                'video': video
            }
            episod_list.append(ep)
        serials.append({
            'name' : name,
            'thumb' : thumb,
            'episods': episod_list
        })
    return JsonResponse(serials, safe=False)
