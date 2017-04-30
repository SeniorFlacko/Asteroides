from django.shortcuts import render

# Create your views here.
from django.views import generic
from unapp.models import Asteroide
import requests
from datetime import date

class AsteroideListView(generic.ListView):
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
            url = nasa_jpl_url,
            is_dangerous = is_potentially_hazardous_asteroid,
        )
        asteroide.save()
    model = Asteroide 


'''   return render(request,"unapp/nibiru.html", {
        'name':name,
        'estimated_diameter_min':estimated_diameter_min,
        'estimated_diameter_max':estimated_diameter_max,
        'is_potentially_hazardous_asteroid': is_potentially_hazardous_asteroid,
        'url_planeta':nasa_jpl_url,
        })'''