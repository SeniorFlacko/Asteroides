# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.urls import reverse
# Create your models here.
class Asteroide(models.Model):
    nombre = models.CharField(max_length=200)
    diametro_min = models.CharField(max_length=200)
    diametro_max = models.CharField(max_length=200)
    fecha = models.DateField()
    url = models.URLField()
    is_dangerous = models.BooleanField()

    def get_absolute_url(self):
        return reverse('asteroide-detail', kwargs={'pk': self.pk})