from pyexpat import model
from statistics import mode
from django.db import models

class Artifiact(models.Model):
    name=models.CharField(max_length=100)
    shiny=models.BooleanField()
