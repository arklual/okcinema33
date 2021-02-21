from django.db import models
class Film(models.Model):
    title = models.CharField(max_length=50)
    date = models.DateField("Дата", auto_now=False)
    description = models.TextField()
    video = models.FileField(null=True, blank=True)
    poster = models.FileField(null=True, blank=True)
    raiting = models.FloatField(default=0, null=True, blank=True)
    numMarks = models.IntegerField(default=0, null=True, blank=True)
    def __str__(self):
        return f"{self.title}"

