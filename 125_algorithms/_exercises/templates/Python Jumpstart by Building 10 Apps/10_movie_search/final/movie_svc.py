_______ c..
_______ requests

MovieResult  c...n..(
    'MovieResult',
    "imdb_code,title,duration,director,year,rating,imdb_score,keywords,genres")


___ find_movies(search_text):

    __ n.. search_text o. n.. search_text.s..:
        r.. ValueError("Search text is required")

    # This URL changed since the recording to support SSL.
    url  'http://movieservice.talkpython.fm/api/search/{}'.f..(search_text)

    resp  requests.get(url)
    resp.raise_for_status()

    movie_data  resp.json()
    movies_list  movie_data.get('hits')

    movies  [
        MovieResult(**md)
        ___ md __ movies_list
    ]

    movies.s..(keylambda m: -m.year)

    r.. movies
