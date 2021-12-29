import json


___ get_movie_data(files: list) -> list:
    """Parse movie json files into a list of dicts"""
    movie_files = []
    for file in files:
        with open(file) as mf:
            data = json.load(mf)
            movie_files.append(data)
    return movie_files
    

___ get_single_comedy(movies: list) -> str:
    """return the movie with Comedy in Genres"""
    for movie in movies:
        __ "Comedy" in movie["Genre"]:
            return movie["Title"]


___ get_movie_most_nominations(movies: list) -> str:
    """Return the movie that had the most nominations"""
    nominations_dict = {}
    for movie in movies:
        nominations_index = movie["Awards"].rfind("nominations")
        nominations_count = movie["Awards"][nominations_index -3: nominations_index]
        
        __ movie["Title"] not in nominations_dict:
            nominations_dict[movie["Title"]] = int(nominations_count)

    return max(nominations_dict, key=nominations_dict.get)


___ get_movie_longest_runtime(movies: list) -> str:
    """Return the movie that has the longest runtime"""
    runtime_dict = {}
    for movie in movies:
        runtime_index = movie["Runtime"].rfind(" min")
        movie_runtime = movie["Runtime"][:runtime_index]

        __ movie["Title"] not in runtime_dict:
            runtime_dict[movie["Title"]] = int(movie_runtime)

    return max(runtime_dict, key=runtime_dict.get)

#if __name__ == "__main__":
    #print(get_movie_most_nominations(get_movie_data(data)))
    #print(get_movie_longest_runtime(get_movie_data(data)))