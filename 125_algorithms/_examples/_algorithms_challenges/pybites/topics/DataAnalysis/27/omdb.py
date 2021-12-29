import json


def get_movie_data(files: list) -> list:
    """Parse movie json files into a list of dicts"""
    data = []
    for movie in files:
        with open(movie) as f:
            for line in f:
                if len(line.strip()) > 0:
                    data.append(json.loads(line.strip()))
    return data

def get_single_comedy(movies: list) -> str:
    """return the movie with Comedy in Genres"""
    for movie in movies:
        #print(movie['Title'])
        if "Comedy" in movie['Genre']:
            return movie['Title']


def get_movie_most_nominations(movies: list) -> str:
    """Return the movie that had the most nominations"""
    # "Awards":"Nominated for 1 Oscar. Another 10 wins & 32 nominations."
    nomination_count = {}
    for movie in movies:
        nomination_count[movie['Title']] = int(movie['Awards'].split()[-2])
    return max(nomination_count, key=nomination_count.get)


def get_movie_longest_runtime(movies: list) -> str:
    """Return the movie that has the longest runtime"""
    #"Runtime":"107 min"
    runtime = {}
    for movie in movies:
        runtime[movie['Title']] = int(movie['Runtime'].split()[0])
    return max(runtime, key=runtime.get)


#files = []
#with open("omdb_data.json") as f:
#    for i, line in enumerate(f.readlines(), 1):
#        movie_json = f'{i}.json'
#        with open(movie_json, 'w') as f:
#            f.write(f'{line}\n')
#        files.append(movie_json)
    

print(len(get_movie_data(['1.json', '2.json', '3.json', '4.json', '5.json'])))

for m in get_movie_data(['1.json', '2.json', '3.json', '4.json', '5.json']):
    print(type(m))

print(get_single_comedy(get_movie_data(['1.json', '2.json', '3.json', '4.json', '5.json'])))

print(get_movie_most_nominations(get_movie_data(['1.json', '2.json', '3.json', '4.json', '5.json'])))

print(get_movie_longest_runtime(get_movie_data(['1.json', '2.json', '3.json', '4.json', '5.json'])))