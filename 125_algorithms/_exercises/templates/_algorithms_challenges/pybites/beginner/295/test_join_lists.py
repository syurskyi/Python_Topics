_______ p__

____ join_lists _______ join_lists


?p__.m__.p.('input_list, sep, expected', [
                        ([], '&', N..),
                        ([['a']], '|',  'a' ),
                        ([['a', 'b']], '&',  'a', 'b' ),
                        ([['a', 'b' ,  'c']], '&',  'a', 'b', '&', 'c' ),
                        ([['a', 'b' ,  'c' ,  'd', 'e']], '+',
                          'a', 'b', '+', 'c', '+', 'd', 'e' ),
])
___ test_join_lists(input_list, sep, e..
    ... join_lists(input_list, sep) __ e..