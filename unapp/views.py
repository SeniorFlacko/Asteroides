from django.shortcuts import render

# Create your views here.
import requests
def planetas(request):
    payload = {'start_date':'2017-04-26', 'end_date':'2017-04-27', 'api_key': 'zLwLUxH607uK27sOyP7H1Y2OF3OigQ3Y1rMMsccJ'}
    r = requests.get('https://api.nasa.gov/neo/rest/v1/feed', params=payload)
    d = r.json()
    neo = d['near_earth_objects']
    name = neo['2017-04-27'][0]['name']
    estimated_diameter_min = neo['2017-04-27'][0]['estimated_diameter']['kilometers']['estimated_diameter_min']
    estimated_diameter_max = neo['2017-04-27'][0]['estimated_diameter']['kilometers']['estimated_diameter_max']
    is_potentially_hazardous_asteroid = neo['2017-04-27'][0]['is_potentially_hazardous_asteroid']
    nasa_jpl_url = neo['2017-04-27'][0]['nasa_jpl_url']
    return render(request,"unapp/nibiru.html", {
        'name':name,
        'estimated_diameter_min':estimated_diameter_min,
        'estimated_diameter_max':estimated_diameter_max,
        'is_potentially_hazardous_asteroid': is_potentially_hazardous_asteroid,
        'url_planeta':nasa_jpl_url,
        })