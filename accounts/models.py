from django.db import models
from django.contrib.auth.models import User

    
# Create your models here.
class Profile(models.Model):
  user = models.OneToOneField(User, on_delete=models.CASCADE, null=False)
  email = models.EmailField(null = True, blank = True)
  image = models.ImageField()
  numberOfMarks = models.IntegerField(default=0)
  numberOfRecensions = models.IntegerField(default=0)
  reputation = models.IntegerField(default=0)
  key = models.IntegerField(default=0)

  def __str__(self):
    return self.user.username