from collections import Counter

import requests

CAR_DATA = 'https://bites-data.s3.us-east-2.amazonaws.com/cars.json'

# pre-work: load JSON data into program

with requests.Session() as s:
    data = s.get(CAR_DATA).json()


# your turn:
def most_prolific_automaker(year):
    """Given year 'year' return the automaker that released
       the highest number of new car models"""
    models_year = ([models for models in data if models['year'] == year])
    count = Counter()
    for models in models_year:
        count[models['automaker']] += 1
    return count.most_common(1)[0][0]



def get_models(automaker, year):
    """Filter cars 'data' by 'automaker' and 'year',
       return a set of models (a 'set' to avoid duplicate models)"""
    automaker_year = ([models for models in data if models['year'] == year and models['automaker'] == automaker])
    return set(model['model'] for model in automaker_year)

#most_prolific_automaker(1999)

#get_models('Nissan', 2000)
print(get_models('Volkswagen', 2008))