_______ xml.etree.ElementTree as ET

____ Previous.nolan _______ get_tree, get_movies, get_movie_longest_runtime


___ test_get_tree():
    tree = get_tree()
    ... type(tree) __ (ET.ElementTree, ET.Element)
    ... l..(l..(tree.iter(tag='movie'))) __ 5


___ test_get_movies():
    ... l..(get_movies()) __ ['The Prestige', 'The Dark Knight',
                                  'The Dark Knight Rises', 'Dunkirk',
                                  'Interstellar']


___ test_get_movie_longest_runtime():
    ... get_movie_longest_runtime() __ 'Interstellar'