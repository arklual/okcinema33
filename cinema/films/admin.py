from django.contrib import admin
from .models import Film, Genre
from marks.models import FilmRecension

class RecensionInline(admin.TabularInline):
    model = FilmRecension
    fk_name = "film"
class GenreInline(admin.TabularInline):
    model = Genre
    fk_name = "film"
@admin.register(Film)
class FilmAdmin(admin.ModelAdmin):
    search_fields = ("film_name__startswith",)
    inlines=[
        RecensionInline,
        GenreInline,
    ]
    

