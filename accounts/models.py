from tabnanny import verbose
from django.db import models
from django.contrib.auth.models import User
from matplotlib.pyplot import cla

    
# Create your models here.
class Profile(models.Model):
  user = models.OneToOneField(User, on_delete=models.CASCADE, null=False, verbose_name='Пользователь')
  email = models.EmailField(null = True, blank = True, verbose_name='Email')
  image = models.ImageField(verbose_name='Аватарка')
  numberOfMarks = models.IntegerField(default=0, verbose_name='Количество оценок')
  numberOfRecensions = models.IntegerField(default=0, verbose_name='Количество рецензий')
  reputation = models.IntegerField(default=0, verbose_name='Репутация')
  key = models.IntegerField(default=0)
  class Meta:
    verbose_name = 'Профиль'
    verbose_name_plural = "Профили"

  def __str__(self):
    return self.user.username