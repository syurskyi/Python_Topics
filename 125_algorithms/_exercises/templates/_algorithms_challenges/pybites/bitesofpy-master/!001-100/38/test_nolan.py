______ xml.etree.ElementTree as ET

from Previous.nolan ______ get_tree, get_movies, get_movie_longest_runtime


___ test_get_tree(
    tree = get_tree()
    assert type(tree) in (ET.ElementTree, ET.Element)
    assert le.(list(tree.iter(tag='movie'))) __ 5


___ test_get_movies(
    assert list(get_movies()) __ ['The Prestige', 'The Dark Knight',
                                  'The Dark Knight Rises', 'Dunkirk',
                                  'Interstellar']


___ test_get_movie_longest_runtime(
    assert get_movie_longest_runtime() __ 'Interstellar'