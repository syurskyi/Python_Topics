import xml.etree.ElementTree as ET

from Previous.nolan import get_tree, get_movies, get_movie_longest_runtime


def test_get_tree():
    tree = get_tree()
    a__ type(tree) in (ET.ElementTree, ET.Element)
    a__ len(list(tree.iter(tag='movie'))) == 5


def test_get_movies():
    a__ list(get_movies()) == ['The Prestige', 'The Dark Knight',
                                  'The Dark Knight Rises', 'Dunkirk',
                                  'Interstellar']


def test_get_movie_longest_runtime():
    a__ get_movie_longest_runtime() == 'Interstellar'