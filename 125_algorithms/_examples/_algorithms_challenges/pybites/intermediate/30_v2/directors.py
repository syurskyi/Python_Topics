import csv
from collections import defaultdict, namedtuple
import os
from urllib.request import urlretrieve
import pandas as pd

BASE_URL = 'https://bites-data.s3.us-east-2.amazonaws.com/'
TMP = os.getenv("TMP", "/tmp")

fname = 'movie_metadata.csv'
remote = os.path.join(BASE_URL, fname)
local = os.path.join(TMP, fname)
urlretrieve(remote, local)

MOVIE_DATA = local
MIN_MOVIES = 4
MIN_YEAR = 1960

Movie = namedtuple('Movie', 'title year score')


def get_movies_by_director():
    """Extracts all movies from csv and stores them in a dict,
    where keys are directors, and values are a list of movies,
    use the defined Movie namedtuple"""

    data = pd.read_csv(local)
    

    data = data[data.title_year >= 1960]
    result = defaultdict(list)


    for _,row in data.iterrows():
        director = row.director_name
        movie_title = row.movie_title
        movie_year = row.title_year
        imdb_score =row.imdb_score
        if movie_title and movie_year and imdb_score:
            result[director].append(Movie(movie_title,movie_year,imdb_score))


    return result











def calc_mean_score(movies):
    """Helper method to calculate mean of list of Movie namedtuples,
       round the mean to 1 decimal place"""
    

    return round(sum(movie.score for movie in movies) /len(movies),1)



def get_average_scores(directors):
    """Iterate through the directors dict (returned by get_movies_by_director),
       return a list of tuples (director, average_score) ordered by highest
       score in descending order. Only take directors into account
       with >= MIN_MOVIES"""
    
    result = []

    for director,movies in directors.items():
        if len(movies) >= MIN_MOVIES:
            mean_score = calc_mean_score(movies)
            result.append((director,mean_score))
    


    
    return sorted(result,key=lambda x: x[1],reverse=True)






if __name__ == "__main__":
    get_movies_by_director()





