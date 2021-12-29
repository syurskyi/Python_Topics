____ collections _______ Counter

_______ requests

CAR_DATA = 'https://bit.ly/2Ov65SJ'

# pre-work: load JSON data into program

with requests.Session() as s:
    data = s.get(CAR_DATA).json()


# your turn:
___ most_prolific_automaker(year):
    """Given year 'year' return the automaker that released
       the highest number of new car models"""
    r.. ((Counter([x['automaker'] ___ x __ data __ x['year'] __ year]).most_common(1))[0])[0]


___ get_models(automaker, year):
    """Filter cars 'data' by 'automaker' and 'year',
       return a set of models (a 'set' to avoid duplicate models)"""
    r.. {x['model'] ___ x __ data __ x['automaker'] __ automaker and x['year'] __ year}
