from django.db import models
from django.conf import settings
from films.models import Film
from serials.models import Serial

class Voter(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    film = models.ForeignKey(Film, on_delete=models.CASCADE)
class SerialVoter(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    serial = models.ForeignKey(Serial, on_delete=models.CASCADE)
class FilmRecension(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    film = models.ForeignKey(Film, on_delete=models.CASCADE)

    title = models.CharField(default='', max_length=120)
    text = models.TextField(default='')
class SerialRecension(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    serial = models.ForeignKey(Serial, on_delete=models.CASCADE)

    title = models.CharField(default='', max_length=120)
    text = models.TextField(default='')