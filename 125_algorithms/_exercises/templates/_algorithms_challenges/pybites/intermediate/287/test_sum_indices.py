_______ p__

____ sum_indices _______ sum_indices


?p__.m__.p.('test_input, expected', [
                        (   # list, 0),
                        ( 'a' , 0),
                        ( 'a', 'b', 'c' , 3),
                        ( 'a', 'b', 'b', 'c' , 7),
                        ( 'a', 'b', 'b', 'c', 'a', 'b', 'a' , 29),
                        ( 'a', 'b', 'c', 'd', 'e', 'a', 'f', 'a', 'g', 'd', 'a' , 75),
                        ( 'a', 'b', 'z', 'c', 'd', 'x', 'b', 'x', 'e' , 42), ])
___ test_sum_indices(test_input, e..
    ... sum_indices(test_input) __ e..