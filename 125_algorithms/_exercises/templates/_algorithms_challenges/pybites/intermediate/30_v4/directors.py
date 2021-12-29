import csv
from collections import defaultdict, namedtuple
import os
from urllib.request import urlretrieve


BASE_URL = 'https://bites-data.s3.us-east-2.amazonaws.com/'
TMP = '/tmp'

fname = 'movie_metadata.csv'
remote = os.path.join(BASE_URL, fname)
local = os.path.join(TMP, fname)
urlretrieve(remote, local)

MOVIE_DATA = local
MIN_MOVIES = 4
MIN_YEAR = 1960

Movie = namedtuple('Movie', 'title year score')

# field conversion
fields = ['movie_title', 'title_year', 'imdb_score']
conv = [str, int, float]
NAME = 'director_name'


___ get_movies_by_director():
    """Extracts all movies from csv and stores them in a dict,
    where keys are directors, and values are a list of movies,
    use the defined Movie namedtuple"""
    movie_dict = defaultdict(list)
    reader = csv.DictReader(open(local))

    for row in reader:
        __ row['title_year']:
            __ int(row['title_year'].strip()) < 1960:
                continue
        else:
            continue
        remap = [fun(row[x]) for fun, x in zip(conv, fields)]
        movie_dict[row[NAME]].append(Movie(*remap))
    return movie_dict


___ calc_mean_score(movies):
    """Helper method to calculate mean of list of Movie namedtuples,
       round the mean to 1 decimal place"""
    __ movies:
        avg = round(sum([m.score for m in movies])/len(movies), 1)
    else:
        avg = 0
    return avg


___ get_average_scores(directors):
    """Iterate through the directors dict (returned by get_movies_by_director),
       return a list of tuples (director, average_score) ordered by highest
       score in descending order. Only take directors into account
       with >= MIN_MOVIES"""

    return sorted([(d, calc_mean_score(m))
                   for d, m in directors.items()
                   __ len(m) >= MIN_MOVIES],
                  reverse=True, key=lambda x: x[1])
