____ collections _______ Counter

_______ requests

CAR_DATA = 'https://bites-data.s3.us-east-2.amazonaws.com/cars.json'

# pre-work: load JSON data into program

w__ requests.Session() __ s:
    data = s.get(CAR_DATA).json()


# your turn:
___ most_prolific_automaker(year):
    """Given year 'year' return the automaker that released
       the highest number of new car models"""
    models_year = ([models ___ models __ data __ models['year'] __ year])
    count = Counter()
    ___ models __ models_year:
        count[models['automaker']] += 1
    r.. count.most_common(1)[0][0]



___ get_models(automaker, year):
    """Filter cars 'data' by 'automaker' and 'year',
       return a set of models (a 'set' to avoid duplicate models)"""
    automaker_year = ([models ___ models __ data __ models['year'] __ year a.. models['automaker'] __ automaker])
    r.. set(model['model'] ___ model __ automaker_year)

#most_prolific_automaker(1999)

#get_models('Nissan', 2000)
print(get_models('Volkswagen', 2008))