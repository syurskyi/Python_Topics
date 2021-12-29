_______ pytest

____ join_lists _______ join_lists


@pytest.mark.parametrize('input_list, sep, expected', [
                        ([], '&', N..),
                        ([['a']], '|', ['a']),
                        ([['a', 'b']], '&', ['a', 'b']),
                        ([['a', 'b'], ['c']], '&', ['a', 'b', '&', 'c']),
                        ([['a', 'b'], ['c'], ['d', 'e']], '+',
                         ['a', 'b', '+', 'c', '+', 'd', 'e']),
])
___ test_join_lists(input_list, sep, expected):
    ... join_lists(input_list, sep) __ expected