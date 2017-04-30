from django.db import models

# Create your models here.

class Asteroide(models.Model):
    nombre = models.CharField(max_length=200)
    diametro_min = models.CharField(max_length=200)
    diametro_max = models.CharField(max_length=200)
    url = models.URLField()
    is_dangerous = models.BooleanField()



