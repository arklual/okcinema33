from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save

    
# Create your models here.
class Profile(models.Model):
  user = models.OneToOneField(User, on_delete=models.CASCADE, null=False)
  email = models.EmailField(null = True, blank = True)
  image = models.ImageField()
  numberOfMarks = models.IntegerField(default=0)
  numberOfRecensions = models.IntegerField(default=0)

  def __str__(self):
    return self.user.username
  def create_user_profile(sender, instance, created, **kwargs):
    if created:
        profile, created = Profile.objects.get_or_create(user=instance)
        profile.email = instance.email
        profile.save()

  post_save.connect(create_user_profile, sender=User)