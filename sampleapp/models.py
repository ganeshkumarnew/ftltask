from django.db import models
from django.contrib.auth.models import User

class UserPlace(models.Model):
    place = models.CharField(max_length=200)
    user = models.ForeignKey(User)
    

class ActivityPeriods(models.Model):
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    user = models.ForeignKey(User)


def __str__(self):
  return self.username



  