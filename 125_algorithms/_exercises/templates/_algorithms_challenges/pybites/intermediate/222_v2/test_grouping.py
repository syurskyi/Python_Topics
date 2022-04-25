_______ types

____ grouping _______ group


___ test_split_10_ints_by_3
    iterable [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    n 3
    a.. g.. iterable, n)
    e.. [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10]]
    ... a.. __ e..


___ test_passing_in_tuple
    iterable (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
    n 3
    a.. g.. iterable, n)
    e.. [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10]]
    ... a.. __ e..


___ test_passing_in_generator
    iterable [1, 2, 3, 4, 5, 6, 7, 8, 9]
    gen (i ___ i __ iterable)
    ... isi..(gen, types.GeneratorType)
    n 3
    a.. g.. gen, n)
    e.. [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    ... a.. __ e..


___ test_different_iterable_size
    iterable [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] * 2
    n 3
    a.. g.. iterable, n)
    e.. [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 1, 2],
                [3, 4, 5], [6, 7, 8], [9, 10]]
    ... a.. __ e..


___ test_different_n
    iterable [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] * 2
    n 5
    a.. g.. iterable, n)
    e.. [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10],
                [1, 2, 3, 4, 5], [6, 7, 8, 9, 10]]
    ... a.. __ e..