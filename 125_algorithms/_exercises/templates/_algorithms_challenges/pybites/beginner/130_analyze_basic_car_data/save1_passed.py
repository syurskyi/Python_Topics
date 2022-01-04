____ c.. _______ Counter
_______ requests

CAR_DATA = 'https://bites-data.s3.us-east-2.amazonaws.com/cars.json'

# load JSON data into program
w__ requests.Session() __ s:
    data = s.get(CAR_DATA).json()

___ most_prolific_automaker(year):
    """Given year 'year' return the automaker that released
       the highest number of new car models"""
    automaker_count = Counter([item['automaker']
            ___ item __ data
            __ item['year'] __ year])
    r.. max(automaker_count, key=automaker_count.get)


___ get_models(automaker, year):
    """Filter cars 'data' by 'automaker' and 'year',
       return a set of models (a 'set' to avoid duplicate models)"""
    find_model = [item['model']
            ___ item __ data
            __ item['year'] __ year
                       a.. item['automaker'] __ automaker]
    r.. set(find_model)