'''
In this Bite you will use ElementTree to parse some Nolan movies we extracted from OMDb.

Luckily most APIs switched to JSON, but sometimes XML is all there is, so at least learn to parse some!
Complete the get_tree, get_movies and get_movie_longest_runtime functions below. See the docstrings and tests for more info.
'''

_______ ___.e__.E__ __ ET

# from OMDB
xmlstring '''<?xml version="1.0" encoding="UTF-8"?>
<root response="True">
  <movie title="The Prestige" year="2006" rated="PG-13" released="20 Oct 2006" runtime="130 min" genre="Drama, Mystery, Sci-Fi" director="Christopher Nolan" />
  <movie title="The Dark Knight" year="2008" rated="PG-13" released="18 Jul 2008" runtime="152 min" genre="Action, Crime, Drama" director="Christopher Nolan" />
  <movie title="The Dark Knight Rises" year="2012" rated="PG-13" released="20 Jul 2012" runtime="164 min" genre="Action, Thriller" director="Christopher Nolan" />
  <movie title="Dunkirk" year="2017" rated="PG-13" released="21 Jul 2017" runtime="106 min" genre="Action, Drama, History" director="Christopher Nolan" />
  <movie title="Interstellar" year="2014" rated="PG-13" released="07 Nov 2014" runtime="169 min" genre="Adventure, Drama, Sci-Fi" director="Christopher Nolan"/>
</root>'''  # noqa E501


___ get_tree
    """You probably want to use ET.fromstring"""
    #tree = ET.fromstring(xmlstring)
    r.. ET.E__(ET.f..(xmlstring
    #return tree

___ get_movies
    """Call get_tree and retrieve all movie titles, return a list or generator"""
    tree get_tree().getroot()
    result    # list
    ___ m __ tree:
        result.a..(m.attrib 'title' )
    r.. result

___ get_movie_longest_runtime
    """Call get_tree again and return the movie with the longest runtime in minutes,
       for latter consider adding a _get_runtime helper"""
    tree get_tree().getroot()
    current_longest_runtime 0
    current_longest_title "None"
    ___ m __ tree:
        __ i..(m.attrib 'runtime' .s.. [0]) > i..(current_longest_runtime
            current_longest_runtime i..(m.attrib 'runtime' .s.. [0])
            current_longest_title m.attrib 'title'

    r.. current_longest_title

print(get_movie_longest_runtime
print(get_movies