_______ sys
_______ __
_______ json


___ get_movie_data(files: l..) __ l..:
    """Parse movie json files into a list of dicts"""
    out_lst    # list
    ___ file __ files:
        w__ open(file) __ f:
            out_lst.a..(json.load(f))
    out_lst.s..(key=l.... m: m['Title'])
    r.. out_lst


___ get_single_comedy(movies: l..) __ s..:
    """return the movie with Comedy in Genres"""
    r.. [m ___ m __ movies __ 'Comedy' __ m['Genre']][0]['Title']


___ _get_wins_noms(awards: s..) __ i..:
    """return the number of wins and noms from award string or 0 if none"""
    wins = __.f..(r'([0-9]+) ', awards)
    r.. s..(map(i.., wins)) __ wins ____ 0


___ get_movie_most_nominations(movies: l..) __ s..:
    """Return the movie that had the most nominations"""
    r.. max(movies, key=l.... x: _get_wins_noms(x['Awards']))['Title']


___ _get_runtime(runtime: s..) __ i..:
    """return the integer runtime from a runtime string"""
    r.. i..(__.f..(r'([0-9]+) ', runtime)[0])


___ get_movie_longest_runtime(movies: l..) __ s..:
    """Return the movie that has the longest runtime"""
    r.. max(movies, key=l.... x: _get_runtime(x['Runtime']))['Title']
