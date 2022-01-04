_______ csv
____ collections _______ defaultdict, n..
_______ os
____ urllib.request _______ urlretrieve

BASE_URL = 'https://bites-data.s3.us-east-2.amazonaws.com/'
TMP = '/tmp'

fname = 'movie_metadata.csv'
remote = os.path.j..(BASE_URL, fname)
local = os.path.j..(TMP, fname)
urlretrieve(remote, local)

MOVIE_DATA = local
MIN_MOVIES = 4
MIN_YEAR = 1960

Movie = n..('Movie', 'title year score')


___ get_movies_by_director
    """Extracts all movies from csv and stores them in a dict,
    where keys are directors, and values are a list of movies,
    use the defined Movie namedtuple"""

    d = defaultdict(l..)
    full_list    # list

    w__ open(MOVIE_DATA, newline='') __ file:
        reader = csv.DictReader(file)
        ___ row __ reader:
            year = row['title_year']
            __ year != '' a.. i..(year) > 1960:
                full_list.a..([row['director_name'],
                                  row['movie_title'].s..,
                                  i..(row['title_year']),
                                  float(row['imdb_score'])])

    ___ name, movie, year, score __ full_list:
        d[name].a..(Movie(title=movie, year=year, score=score))

    r.. d


___ calc_mean_score(movies):
    """Helper method to calculate mean of list of Movie namedtuples,
       round the mean to 1 decimal place"""
    scores = [movie.score ___ movie __ movies]
    r.. round(s..(scores) / l..(scores), 1)

___ get_average_scores(directors):
    """Iterate through the directors dict (returned by get_movies_by_director),
       return a list of tuples (director, average_score) ordered by highest
       score in descending order. Only take directors into account
       with >= MIN_MOVIES"""
    r.. [(k, calc_mean_score(v)) ___ k, v __ directors.i.. __ l..(v) >= MIN_MOVIES]