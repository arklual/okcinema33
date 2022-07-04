from django.db import models

class Serial(models.Model):
    title = models.CharField(max_length=50, default="", verbose_name='Название')
    kp_id = models.CharField(max_length=70, null=True, blank=True, verbose_name='КиноПоиск id')
    date = models.DateField(auto_now=False, verbose_name='Дата')
    description = models.TextField(default="", verbose_name='Описание')
    count_sesonov = models.IntegerField(default=1, verbose_name='Количество сезонов')
    poster = models.FileField(null=True, blank=True, verbose_name='Постер')
    raiting = models.FloatField(default=0, null=True, blank=True, verbose_name='Рейтинг')
    numMarks = models.IntegerField(default=0, null=True, blank=True, verbose_name='Количество оценок')
    class Meta:
        verbose_name = 'Сериал'
        verbose_name_plural = 'Сериалы'
    def __str__(self):
        return f"{self.title}"
    
    def get_class_name(self):
        return "Serial"

class Seriya(models.Model):
    serial = models.ForeignKey(Serial,default="", on_delete=models.CASCADE, verbose_name='Сериал')
    season = models.IntegerField(verbose_name='Сезон')
    number = models.IntegerField(verbose_name='Номер')
    title = models.CharField(max_length=50, default="", verbose_name='Название')
    video = models.URLField(null=True, blank=True, verbose_name='Видео')
    class Meta:
        verbose_name = 'Серия'
        verbose_name_plural = 'Серии'
    def __str__(self):
        return f"{self.number}.{self.title}"
