from django.http import JsonResponse
from django.shortcuts import render
from films.models import Film


def movie_list(request):
    films = Film.objects.all()
    movies = []
    for film in films:
        name = film.title
        thumb = film.poster.url
        video = film.video
        genre = 'Жанр'
        movies.append({
            'name' : name,
            'thumb' : thumb,
            'video' : video,
            'genre' : genre
        })
    
    return JsonResponse(movies, safe=False)