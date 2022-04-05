_______ p__

____ intersection _______ intersection


?p__.m__.p.(
    "inputs,expected",
    [
        [({1, 2, 3}, {2, 3, 4}, {3, 4}), {3}],
        [([1, 2, 3, 1], {1, -1}, {}), {1}],
        [({1, "2", "3"}, {1, "3"}), {1, "3"}],
        [
            # mixing lists/sets/tuples
            ([1, 2, 3, 4, 5, 1, 2, 3, 2, 3], {0, 10, 5}, ("a", 5,
            {
                5,
            },
        ],
        [("do you like this bite?", "i hope so"), {"o", "i", "h", "e", "s", " "}],
    ],
)
___ test_basic(inputs, e..
    results = i.. *inputs)
    ... results __ e..


?p__.m__.p.(
    "inputs,expected",
    [
        [((N.., "this is a string", {" ", "a", "g", "h", "i", "n", "r", "s", "t"}],
        [
            # no input
            (N..,),
            s..(),
        ],
        [
            # multiple None inputs
            (N.., {1, 2, 3}, N.., l..(r..(10, N..),
            {1, 2, 3},
        ],
        [([1, 2, 3, 3, 2, 1],), {1, 2, 3}],  # single input
    ],
)
___ test_edgecases(inputs, e..
    results = i.. *inputs)
    ... results __ e..
