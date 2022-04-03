import csv
from collections import defaultdict, namedtuple
import os
from u__.r.. import u..

BASE_URL = 'https://bites-data.s3.us-east-2.amazonaws.com/'
TMP = os.getenv("TMP", "/tmp")

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

    movie_metadata = defaultdict(list)

    with open(local) as file:
        csv_content = csv.DictReader(file)

        for row in csv_content:

            if row["title_year"] != "":
                title_year = int(row["title_year"])
            else:
                continue

            if title_year > MIN_YEAR:
                director_name = row["director_name"]
                movie_title = row["movie_title"].strip()
                imdb_score = float(row["imdb_score"])

                if director_name not in movie_metadata:
                    movie_metadata[director_name] = [Movie(movie_title, title_year, imdb_score)]
                else:
                    movie_metadata[director_name].append(Movie(movie_title, title_year, imdb_score))

    return movie_metadata


def calc_mean_score(movies):
    """Helper method to calculate mean of list of Movie namedtuples,
       round the mean to 1 decimal place"""
    movie_mean = [movie.score for movie in movies]
    return round(sum(movie_mean) / len(movie_mean), 1)    


def get_average_scores(directors):
    """Iterate through the directors dict (returned by get_movies_by_director),
       return a list of tuples (director, average_score) ordered by highest
       score in descending order. Only take directors into account
       with >= MIN_MOVIES"""
    directors_scores = []
    for key, value in directors.items():
        director_avg_score = calc_mean_score(value)
        if len(value) >= MIN_MOVIES:
            directors_scores.append((key, director_avg_score))
    return sorted(directors_scores, key=lambda x: x[1], reverse=True)


# if __name__ == "__main__":
#     test = get_movies_by_director()
#     print(calc_mean_score(test['Sergio Leone']))
#     print(get_average_scores(test))