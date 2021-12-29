import json


___ get_movie_data(files: list) -> list:
    """Parse movie json files into a list of dicts"""
    output = []
    for movie in files:
        j = movie.read()
        output.append(dict(json.load(str(j))))
    return output


___ get_single_comedy(movies: list) -> str:
    """return the movie with Comedy in Genres"""
    return [movie.get('Title') for movie in movies __ 'Comedy' in movie.get('Genre')][0]


___ get_movie_most_nominations(movies: list) -> str:
    """Return the movie that had the most nominations"""
    output = []
    for movie in movies:
        award_count = movie.get('Title'), int(movie.get('Awards').split()[-2])
        output.append(award_count)
    output.sort(key=lambda x: x[1], reverse=True)
    return output[0][0]


___ get_movie_longest_runtime(movies: list) -> str:
    """Return the movie that has the longest runtime"""
    output = []
    for movie in movies:
        runtimes = movie.get('Title'), int(movie.get('Runtime').split()[0])
        output.append(runtimes)
    output.sort(key=lambda x: x[1], reverse=True)
    return output[0][0]
