import json
import random
import os
import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'pandafinder.settings')

import django

django.setup()

import requests

url = "https://wyre-data.p.rapidapi.com"

headers = {
    'x-rapidapi-host': "wyre-data.p.rapidapi.com",
    'x-rapidapi-key': "4c12fb0e81msh3dae3017c496deap1414ccjsnae9bfbb20958"
}

response = requests.request("GET", "https://wyre-data.p.rapidapi.com/restaurants/town/glasgow", headers=headers)
info_list = response.json()

#os.chdir(json_file_save_path)
with open("restaurant_info.json", 'w') as f:
    json.dump(info_list, f)

with open("restaurant_info.json") as f2:
    restaurant_dict = json.load(f2)

print(restaurant_dict[0])