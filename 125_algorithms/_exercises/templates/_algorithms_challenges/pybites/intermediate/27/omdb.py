_______ json


___ get_movie_data(files: l..) -> l..:
    """Parse movie json files into a list of dicts"""
    movie_files    # list
    ___ file __ files:
        with open(file) as mf:
            data = json.load(mf)
            movie_files.a..(data)
    r.. movie_files
    

___ get_single_comedy(movies: l..) -> s..:
    """return the movie with Comedy in Genres"""
    ___ movie __ movies:
        __ "Comedy" __ movie["Genre"]:
            r.. movie["Title"]


___ get_movie_most_nominations(movies: l..) -> s..:
    """Return the movie that had the most nominations"""
    nominations_dict = {}
    ___ movie __ movies:
        nominations_index = movie["Awards"].rfind("nominations")
        nominations_count = movie["Awards"][nominations_index -3: nominations_index]
        
        __ movie["Title"] n.. __ nominations_dict:
            nominations_dict[movie["Title"]] = int(nominations_count)

    r.. max(nominations_dict, key=nominations_dict.get)


___ get_movie_longest_runtime(movies: l..) -> s..:
    """Return the movie that has the longest runtime"""
    runtime_dict = {}
    ___ movie __ movies:
        runtime_index = movie["Runtime"].rfind(" min")
        movie_runtime = movie["Runtime"][:runtime_index]

        __ movie["Title"] n.. __ runtime_dict:
            runtime_dict[movie["Title"]] = int(movie_runtime)

    r.. max(runtime_dict, key=runtime_dict.get)

#if __name__ == "__main__":
    #print(get_movie_most_nominations(get_movie_data(data)))
    #print(get_movie_longest_runtime(get_movie_data(data)))