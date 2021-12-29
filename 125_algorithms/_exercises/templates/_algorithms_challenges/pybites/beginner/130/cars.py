____ collections _______ Counter
_______ pandas as pd

_______ requests

CAR_DATA = 'https://bites-data.s3.us-east-2.amazonaws.com/cars.json'

# pre-work: load JSON data into program


data = requests.get(CAR_DATA).json()

data = pd.DataFrame(data)

# your turn:
___ most_prolific_automaker(year):
    """Given year 'year' return the automaker that released
       the highest number of new car models"""

    r.. data[data.year __ year].automaker.value_counts().idxmax()


___ get_models(automaker, year):
    """Filter cars 'data' by 'automaker' and 'year',
       return a set of models (a 'set' to avoid duplicate models)"""

    r.. set(data.loc[(data.year __ year) & (data.automaker __ automaker),'model'])






