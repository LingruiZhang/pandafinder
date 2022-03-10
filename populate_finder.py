import random
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','pandafinder.settings')

import django
django.setup()

import requests

url = "https://wyre-data.p.rapidapi.com"

headers = {
    'x-rapidapi-host': "wyre-data.p.rapidapi.com",
    'x-rapidapi-key': "4c12fb0e81msh3dae3017c496deap1414ccjsnae9bfbb20958"
    }


from finder.models import Category, Restaurant

response = requests.request("GET", "https://wyre-data.p.rapidapi.com/restaurants/town/glasgow", headers=headers)
print(response.text)

def populate():
