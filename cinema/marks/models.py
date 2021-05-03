from django.db import models
from django.conf import settings
from films.models import Film
from serials.models import Serial
from ckeditor.fields import RichTextField

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
    text = RichTextField(blank=True,null=True)
class SerialRecension(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    serial = models.ForeignKey(Serial, on_delete=models.CASCADE)

    title = models.CharField(default='', max_length=120)
    text = RichTextField(blank=True,null=True)