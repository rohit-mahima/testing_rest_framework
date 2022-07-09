from tkinter import CASCADE
from django.db import models

class Vehicles(models.Model):
    name=models.CharField(max_length=100)

class Part(models.Model):
    name=models.CharField(max_length=100)
    make=models.CharField(max_length=100)
    vehicle=models.ForeignKey(Vehicles, on_delete=CASCADE)