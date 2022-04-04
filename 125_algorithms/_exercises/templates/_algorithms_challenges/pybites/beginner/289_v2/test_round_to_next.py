____ r__ _______ choice

_______ p__

____ round_to_next _______ round_to_next


?p__.m__.p.('test_input, expected', [
                        ((0, 5), 0),
                        ((2, 5), 5),
                        ((5, 5), 5),
                        ((42, 5), 45),
                        ((-6, 10), 0),
                        ((-6, -10), -10),
                        ((-10, 10), -10),
                        ((-10, -10), -10),
                        ((17, 1), 17),
                        ((12_345, 42), 12348),
                        ((15, choice([3, 5, 15], 15),
                         ])
___ test_round_to_next(test_input, expected
    ... round_to_next(*test_input) __ expected