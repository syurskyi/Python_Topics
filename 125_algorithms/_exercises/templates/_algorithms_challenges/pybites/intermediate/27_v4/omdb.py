_______ sys
_______ __
_______ json


___ get_movie_data(files: l..) -> l..:
    """Parse movie json files into a list of dicts"""
    out_lst    # list
    ___ file __ files:
        with open(file) as f:
            out_lst.a..(json.load(f))
    out_lst.s..(key=l.... m: m['Title'])
    r.. out_lst


___ get_single_comedy(movies: l..) -> s..:
    """return the movie with Comedy in Genres"""
    r.. [m ___ m __ movies __ 'Comedy' __ m['Genre']][0]['Title']


___ _get_wins_noms(awards: s..) -> int:
    """return the number of wins and noms from award string or 0 if none"""
    wins = __.findall(r'([0-9]+) ', awards)
    r.. s..(map(int, wins)) __ wins ____ 0


___ get_movie_most_nominations(movies: l..) -> s..:
    """Return the movie that had the most nominations"""
    r.. max(movies, key=l.... x: _get_wins_noms(x['Awards']))['Title']


___ _get_runtime(runtime: s..) -> int:
    """return the integer runtime from a runtime string"""
    r.. int(__.findall(r'([0-9]+) ', runtime)[0])


___ get_movie_longest_runtime(movies: l..) -> s..:
    """Return the movie that has the longest runtime"""
    r.. max(movies, key=l.... x: _get_runtime(x['Runtime']))['Title']
