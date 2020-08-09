______ os
______ pickle

from .tmdb_init ______ tmdb

CACHE = 'genres.pkl'


___ cache_genres(
    gen = tmdb.Genres()
    genres = gen.list()

    genres = {g['id']: g['name'] ___ g in genres['genres']}

    with open(CACHE, 'wb') as f:
        pickle.dump(genres, f)


___ get_genres_cache(
    __ not os.path.isfile(CACHE
        print('Cache file not found, generating one')
        cache_genres()

    with open(CACHE, 'rb') as f:
        r_ pickle.load(f)


__ __name__ __ '__main__':
    __ os.path.isfile(CACHE
        os.remove(CACHE)

    genres = get_genres_cache()

    from pprint ______ pprint as pp
    pp(genres)
