from django.contrib import admin

from .models import Film, Serial, Seriya
# Register your models here.

@admin.register(Film)
class FilmAdmin(admin.ModelAdmin):
    search_fields = ("film_name__startswith", )

@admin.register(Serial)
class SerialAdmin(admin.ModelAdmin):
    search_fields = ("title__startswith", )
    
@admin.register(Seriya)
class SeriyaAdmin(admin.ModelAdmin):
    search_fields = ("title__startswith", "number__startswith")