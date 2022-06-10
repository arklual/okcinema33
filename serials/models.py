from django.db import models

class Serial(models.Model):
    title = models.CharField(max_length=50, default="")
    kp_id = models.CharField(max_length=70, null=True, blank=True)
    date = models.DateField("Дата", auto_now=False)
    description = models.TextField(default="")
    count_sesonov = models.IntegerField(default=1)
    poster = models.FileField(null=True, blank=True)
    raiting = models.FloatField(default=0, null=True, blank=True)
    numMarks = models.IntegerField(default=0, null=True, blank=True)
    def __str__(self):
        return f"{self.title}"
class Seriya(models.Model):
    serial = models.ForeignKey(Serial,default="", on_delete=models.CASCADE)
    season = models.IntegerField()
    number = models.IntegerField()
    title = models.CharField(max_length=50, default="")
    video = models.URLField(null=True, blank=True)
    def __str__(self):
        return f"{self.number}.{self.title}"
