from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Profile(models.Model):
  user = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
  email = models.EmailField(null = True, blank = True)
  image = models.ImageField()

  def __str__(self):
    return self.user.username
