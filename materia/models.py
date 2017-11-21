from django.db import models

# Create your models here.
from django.db import models
from django.utils import timezone

class Materia(models.Model):
    nombre = models.CharField(max_length=50)
    profesor = models.CharField(max_length=200)
    nota = models.IntegerField()

    def __str__(self):
        return self.nombre
