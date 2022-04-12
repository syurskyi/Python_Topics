_______ csv
____ c.. _______ d.., n..
_______ __
____ u__.r.. _______ u..

BASE_URL 'https://bites-data.s3.us-east-2.amazonaws.com/'
TMP __.g.. TMP  /tmp

fname 'movie_metadata.csv'
remote __.p...j..(BASE_URL, fname)
local __.p...j..(TMP, fname)
u.. ? ?

MOVIE_DATA local
MIN_MOVIES 4
MIN_YEAR 1960

Movie n..('Movie', 'title year score')


___ get_movies_by_director
    """Extracts all movies from csv and stores them in a dict,
    where keys are directors, and values are a list of movies,
    use the defined Movie namedtuple"""
    directors d..(l..)
    w__ o.. MOVIE_DATA) __ f:
        ___ line __ csv.DictReader(f
            ___
                director line 'director_name'
                movie line 'movie_title' .r..('\xa0', '')
                year i..(line 'title_year' )
                score f__(line 'imdb_score' )
            ______ V..
                _____
            __ year a.. year < MIN_YEAR:
                _____

            m Movie(title=movie, year=year, score=score)
            directors[director].a..(m)

    r.. directors


___ calc_mean_score(movies
    """Helper method to calculate mean of list of Movie namedtuples,
       round the mean to 1 decimal place"""
    ratings [m.score ___ m __ movies]
    mean s..(ratings) / m..(1, l..(ratings
    r.. r..(mean, 1)


___ get_average_scores(directors
    """Iterate through the directors dict (returned by get_movies_by_director),
       return a list of tuples (director, average_score) ordered by highest
       score in descending order. Only take directors into account
       with >= MIN_MOVIES"""
    ret {director: calc_mean_score(movies)
           ___ director, movies __ directors.i..
           __ l..(movies) >_ MIN_MOVIES}
    r.. s..(ret.i.., key=l.... x: ? 1 r.._T..