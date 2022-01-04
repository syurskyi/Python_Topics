_______ requests
_______ c..

MovieResult  c...n..(
    'MovieResult',
    "imdb_code,title,duration,director,year,rating,imdb_score,keywords,genres")

s..  input("What movie do you want to search for? ")
url  'http://movie_service.talkpython.fm/api/search/{}'.f..(s..)

resp  requests.get(url)
resp.raise_for_status()

movie_data  resp.json()
movies_list  movie_data.get('hits')

# movies = []
# for md in movies_list:
#     m = MovieResult(
#         imdb_code=md.get('imdb_code'),
#         title=md.get('title'),
#         duration=md.get('duration'),
#         director=md.get('director'),
#         year=md.get('year', 0),
#         rating=md.get('rating', 0),
#         imdb_score=md.get('imdb_score', 0.0),
#         keywords=md.get('keywords'),
#         genres=md.get('genres')
#     )
#     movies.append(m)

# def method(x, y, z, **kwargs):
#     print("kwargs=", kwargs)
#
# method(7, 1, z=2, format=True, age=7)

# movies = []
# for md in movies_list:
#     m = MovieResult(**md)
#     movies.append(m)

movies  [
    MovieResult(**md)
    ___ md __ movies_list
]

print("Found {} movies for search {}".f..(l..(movies), s..))
___ m __ movies:
    print("{} -- {}".f..(m.year, m.title))
