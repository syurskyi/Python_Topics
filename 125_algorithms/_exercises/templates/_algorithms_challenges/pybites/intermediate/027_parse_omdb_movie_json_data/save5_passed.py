_______ json


___ get_movie_data(files: l..) -> l..:
    """Parse movie json files into a list of dicts"""
    output    # list
    ___ movie __ files:
        output.a..(d..(json.load(open(movie))))
    r.. output

___ get_single_comedy(movies: l..) -> s..:
    """return the movie with Comedy in Genres"""
    r.. [movie.get('Title') ___ movie __ movies __ 'Comedy' __ movie.get('Genre')][0]


___ get_movie_most_nominations(movies: l..) -> s..:
    """Return the movie that had the most nominations"""
    output    # list
    ___ movie __ movies:
        award_count = movie.get('Title'), int(movie.get('Awards').s.. [-2])
        output.a..(award_count)
    output.s..(key=l.... x: x[1], r.._T..
    r.. output[0][0]


___ get_movie_longest_runtime(movies: l..) -> s..:
    """Return the movie that has the longest runtime"""
    output    # list
    ___ movie __ movies:
        runtimes = movie.get('Title'), int(movie.get('Runtime').s.. [0])
        output.a..(runtimes)
    output.s..(key=l.... x: x[1], r.._T..
    r.. output[0][0]
