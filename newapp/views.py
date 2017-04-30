# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.views.generic.detail import DetailView
from django.views.generic.dates import (
                                        YearArchiveView,
                                        MonthArchiveView,
                                        WeekArchiveView,
                                        DayArchiveView,
                                        TodayArchiveView,
                                        )

# Create your views here.
from datetime import date
import requests
from models import Asteroide

class AsteroideDetailView(DetailView):
    model = Asteroide

class AsteroideYearArchiveView(YearArchiveView):
    queryset = Asteroide.objects.all()
    date_field = "fecha"
    make_object_list = True
    allow_future = True

class AsteroideMonthArchiveView(MonthArchiveView):
    queryset = Asteroide.objects.all()
    date_field = "fecha"
    allow_future = True

class AsteroideWeekArchiveView(WeekArchiveView):
    queryset = Asteroide.objects.all()
    date_field = "fecha"
    week_format = "%W"
    allow_future = True


class AsteroideDayArchiveView(DayArchiveView):
    queryset = Asteroide.objects.all()
    date_field = "fecha"
    allow_future = True

class AsteroideTodayArchiveView(TodayArchiveView):
    hoy = date.today()
    payload = {'start_date':str(hoy), 'end_date':str(hoy), 'api_key': 'zLwLUxH607uK27sOyP7H1Y2OF3OigQ3Y1rMMsccJ'}
    r = requests.get('https://api.nasa.gov/neo/rest/v1/feed', params=payload)
    d = r.json()
    count = d['element_count']
    neo = d['near_earth_objects']
    for i in range(count):
        name = neo[str(hoy)][i]['name']
        estimated_diameter_min = neo[str(hoy)][i]['estimated_diameter']['kilometers']['estimated_diameter_min']
        estimated_diameter_max = neo[str(hoy)][i]['estimated_diameter']['kilometers']['estimated_diameter_max']
        is_potentially_hazardous_asteroid = neo[str(hoy)][i]['is_potentially_hazardous_asteroid']
        nasa_jpl_url = neo[str(hoy)][i]['nasa_jpl_url']
        asteroide = Asteroide.objects.create(
            nombre = name,
            diametro_min =  estimated_diameter_min,
            diametro_max =  estimated_diameter_max,
            fecha = hoy,
            url = nasa_jpl_url,
            is_dangerous = is_potentially_hazardous_asteroid,
        )
    asteroide.save()
    queryset = Asteroide.objects.all()
    date_field = "fecha"
    allow_future = True
