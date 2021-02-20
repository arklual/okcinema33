from django.db import models
from django.conf import settings
from django.db import models
class Film(models.Model):
    title = models.CharField(max_length=50)
    date = models.DateField("Дата", auto_now=False)
    description = models.TextField()
    video = models.FileField(null=True, blank=True)
    poster = models.FileField(null=True, blank=True)
    raiting = models.FloatField(default=0, null=True, blank=True)
    numMarks = models.IntegerField(default=0, null=True, blank=True)
    def get_p_absolute_url(self):
        return "play/"+str(self.id)+"/1"+"/1"
    def get_absolute_url(self):
        return "/%s/" %(self.id)
    def __str__(self):
        return f"{self.title}"

class Serial(models.Model):
    title = models.CharField(max_length=50, default="")
    date = models.DateField("Дата", auto_now=False)
    description = models.TextField(default="")
    count_sesonov = models.IntegerField(default=1)
    poster = models.FileField(null=True, blank=True)
    raiting = models.FloatField(default=0, null=True, blank=True)
    numMarks = models.IntegerField(default=0, null=True, blank=True)
    def __str__(self):
        return f"{self.title}"
    def get_absolute_url(self):
        return "/serial/%s/" %(self.id)

class Seriya(models.Model):
    serial = models.ForeignKey(Serial,default="", on_delete=models.CASCADE)
    title = models.CharField(max_length=50, default="")
    number = models.IntegerField()
    season = models.IntegerField()
    video = models.FileField(null=True, blank=True)
    def __str__(self):
        return f"{self.number}.{self.title}"
    def get_absolute_url(self):
        return "play/"+str(self.id)+"/"+str(self.season)+"/"+str(self.number)
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