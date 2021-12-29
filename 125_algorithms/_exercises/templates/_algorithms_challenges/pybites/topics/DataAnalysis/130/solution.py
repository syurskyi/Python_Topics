____ collections _______ Counter

_______ requests

CAR_DATA = 'https://bites-data.s3.us-east-2.amazonaws.com/cars.json'

# pre-work: load JSON data into program

with requests.Session() as s:
    data = s.get(CAR_DATA).json()


# your turn:
___ most_prolific_automaker(year):
    """Given year 'year' return the automaker that released
       the highest number of new car models"""
    cnt = Counter(row["automaker"] ___ row __ data
                  __ row["year"] __ year).most_common()
    r.. cnt[0][0]


___ get_models(automaker, year):
    """Filter cars 'data' by 'automaker' and 'year',
       return a set of models (a 'set' to avoid duplicate models)"""
    r.. set([row["model"] ___ row __ data
                __ row["automaker"] __ automaker and
                row["year"] __ year])