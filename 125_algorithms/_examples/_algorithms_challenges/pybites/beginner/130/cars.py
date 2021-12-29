from collections import Counter
import pandas as pd

import requests

CAR_DATA = 'https://bites-data.s3.us-east-2.amazonaws.com/cars.json'

# pre-work: load JSON data into program


data = requests.get(CAR_DATA).json()

data = pd.DataFrame(data)

# your turn:
def most_prolific_automaker(year):
    """Given year 'year' return the automaker that released
       the highest number of new car models"""

    return data[data.year == year].automaker.value_counts().idxmax()


def get_models(automaker, year):
    """Filter cars 'data' by 'automaker' and 'year',
       return a set of models (a 'set' to avoid duplicate models)"""

    return set(data.loc[(data.year == year) & (data.automaker == automaker),'model'])






