from tabnanny import verbose
from django.db import models
class Film(models.Model):
    title = models.CharField(max_length=50, verbose_name='Название')
    kp_id = models.CharField(max_length=70, null=True, blank=True, verbose_name='КиноПоиск id')
    date = models.DateField(auto_now=False, verbose_name='Дата')
    description = models.TextField(verbose_name='Описание')
    video = models.URLField(null=True, blank=True, verbose_name='Видео')
    poster = models.FileField(null=True, blank=True, verbose_name='Постер')
    raiting = models.FloatField(default=0, null=True, blank=True, verbose_name='Рейтинг')
    numMarks = models.IntegerField(default=0, null=True, blank=True, verbose_name='Количество оценок')  
    class Meta:
        verbose_name = 'Фильм'
        verbose_name_plural = 'Фильмы'
    def __str__(self):
        return f"{self.title}"
    def get_class_name(self):
        return 'Film'

class Genre(models.Model):
    name = models.CharField(max_length=50, verbose_name='Название')
    film = models.ForeignKey(Film, on_delete=models.CASCADE, verbose_name='Фильм')
    class Meta:
        verbose_name = 'Жанр'
        verbose_name_plural = 'Жанры'