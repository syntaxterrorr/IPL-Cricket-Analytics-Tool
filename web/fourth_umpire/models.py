from django.db import models
from django.utils import timezone
# Create your models here.

class Match(models.Model):
    team1 = models.CharField(max_length=30)
    team2 = models.CharField(max_length=30)
    playinxi = models.CharField(max_length=50)
# class Playinxi(models.Model):
#     playinxi = models.ForeignKey(Match, on_delete=models.CASCADE)
