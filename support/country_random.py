import os
import json
import random

ROOT_PATH = os.path.dirname(os.path.realpath(__file__))
path = os.path.join(ROOT_PATH, "country_codes.json")

with open(path, 'r') as f:
    country_data = json.load(f)

country_names = [country['name'] for country in country_data]
random_country = random.choice(country_names)