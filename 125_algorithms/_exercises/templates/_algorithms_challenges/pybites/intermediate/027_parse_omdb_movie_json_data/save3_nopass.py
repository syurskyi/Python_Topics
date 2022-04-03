_______ json


___ get_movie_data(files: l..) __ l..:
    """Parse movie json files into a list of dicts"""
    output    # list
    ___ movie __ files:
        output.a..(d..(json.load(movie)))
    r.. output


___ get_single_comedy(movies: l..) __ s..:
    """return the movie with Comedy in Genres"""
    r.. [movie.g.. 'Title') ___ movie __ movies __ 'Comedy' __ movie.g.. 'Genre')][0]


___ get_movie_most_nominations(movies: l..) __ s..:
    """Return the movie that had the most nominations"""
    output    # list
    ___ movie __ movies:
        award_count = movie.g.. 'Title'), i..(movie.g.. 'Awards').s.. [-2])
        output.a..(award_count)
    output.s..(key=l.... x: x[1], r.._T..
    r.. output[0][0]


___ get_movie_longest_runtime(movies: l..) __ s..:
    """Return the movie that has the longest runtime"""
    output    # list
    ___ movie __ movies:
        runtimes = movie.g.. 'Title'), i..(movie.g.. 'Runtime').s.. [0])
        output.a..(runtimes)
    output.s..(key=l.... x: x[1], r.._T..
    r.. output[0][0]
