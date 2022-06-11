from django.http import JsonResponse
from django.shortcuts import render
from films.models import Film, Genre

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
            genre += i
        movies.append({
            'name' : name,
            'thumb' : thumb,
            'video' : video,
            'genre' : genre
        })
    
    return JsonResponse(movies, safe=False)