import csv
from collections import defaultdict, namedtuple
import os
from urllib.request import urlretrieve

BASE_URL = 'https://bites-data.s3.us-east-2.amazonaws.com/'
TMP = os.getenv("TMP", "/tmp")

fname = 'movie_metadata.csv'
#remote = os.path.join(BASE_URL, fname)
local = os.path.join(TMP, fname)
#urlretrieve(remote, local)

MOVIE_DATA = local
MIN_MOVIES = 4
MIN_YEAR = 1960

Movie = namedtuple('Movie', 'title year score')


def get_movies_by_director():
    """Extracts all movies from csv and stores them in a dict,
    where keys are directors, and values are a list of movies,
    use the defined Movie namedtuple"""
    director = defaultdict(list)
    with open(local, encoding="utf-8") as f:
        movies = csv.DictReader(f)
        for movie in movies:
            if movie['title_year'] != '' and int(movie['title_year']) > 1960:
                director[movie['director_name']].append(
                    Movie(
                        movie['movie_title'].strip(),
                        movie['title_year'], 
                        movie['imdb_score'])
                )
    return director


def calc_mean_score(movies):
    """Helper method to calculate mean of list of Movie namedtuples,
       round the mean to 1 decimal place"""
    total = 0
    for movie in movies:
        total += float(movie[2])
    return round(total/len(movies), 1)


def get_average_scores(directors):
    """Iterate through the directors dict (returned by get_movies_by_director),
       return a list of tuples (director, average_score) ordered by highest
       score in descending order. Only take directors into account
       with >= MIN_MOVIES"""
    #print(len(directors))
    local_list = []
    for director in directors:
        if len(directors[director]) >= MIN_MOVIES: # each director
            total = 0
            for i in range(len(directors[director])): 
                #print(director, int(directors[director][i][1]))
                if directors[director][i][1] and int(directors[director][i][1]) >1960:
                    total += float(directors[director][i][2])
            local_list.append((director, round(total/len(directors[director]),1)))
    return sorted(local_list, key=lambda x: x[1], reverse=True)


director_dict = get_movies_by_director()
#print(len(director_dict))
#print(type(director_dict['Sergio Leone'][0]))

#print(director_dict["Lowell Sherman"])

#print(calc_mean_score(director_dict['Hayao Miyazaki']))

print(get_average_scores(director_dict))