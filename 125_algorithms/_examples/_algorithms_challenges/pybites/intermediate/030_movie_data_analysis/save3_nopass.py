import csv
from collections import defaultdict, namedtuple
import os
from u__.r.. import u..

BASE_URL = 'https://bites-data.s3.us-east-2.amazonaws.com/'
TMP = '/tmp'

fname = 'movie_metadata.csv'
remote = os.path.join(BASE_URL, fname)
local = os.path.join(TMP, fname)
u..(remote, local)

MOVIE_DATA = local
MIN_MOVIES = 4
MIN_YEAR = 1960

Movie = namedtuple('Movie', 'title year score')


def get_movies_by_director():
    """Extracts all movies from csv and stores them in a dict,
    where keys are directors, and values are a list of movies,
    use the defined Movie namedtuple"""

    d = defaultdict(list)
    full_list = []

    with open(MOVIE_DATA, newline='') as file:
        reader = csv.DictReader(file)
        for row in reader:
            year = row['title_year']
            if year != '' and int(year) > 1960:
                full_list.append([row['director_name'],
                                  row['movie_title'].strip(),
                                  int(row['title_year']),
                                  float(row['imdb_score'])])

    for name, movie, year, score in full_list:
        d[name].append(Movie(title=movie, year=year, score=score))

    return d


def calc_mean_score(movies):
    """Helper method to calculate mean of list of Movie namedtuples,
       round the mean to 1 decimal place"""
    scores = [movie.score for movie in movies]
    return round(sum(scores) / len(scores), 1)

def get_average_scores(directors):
    """Iterate through the directors dict (returned by get_movies_by_director),
       return a list of tuples (director, average_score) ordered by highest
       score in descending order. Only take directors into account
       with >= MIN_MOVIES"""

    director_list = []
    for director in directors:
        if len(get_movies_by_director()[director]) >= MIN_MOVIES:
            d_tuple = director, calc_mean_score(get_movies_by_director()[director])
            director_list.append(d_tuple)

    director_list.sort(key=lambda a: a[1], reverse=True)

    return director_list
