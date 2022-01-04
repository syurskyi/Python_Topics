____ rotate _______ rotate


___ test_small_rotate
    ... rotate('hello', 2) __ 'llohe'
    ... rotate('hello', -2) __ 'lohel'


___ test_bigger_rotation_of_positive_n
    string = 'bob and julian love pybites!'
    expected = 'love pybites!bob and julian '
    ... rotate(string, 15) __ expected


___ test_bigger_rotation_of_negative_n
    string = 'pybites loves julian and bob!'
    expected = 'julian and bob!pybites loves '
    ... rotate(string, -15) __ expected


___ test_rotation_of_n_same_as_len_str
    string = expected = 'julian and bob!'
    ... rotate(string, l..(string)) __ expected


___ test_rotation_of_n_bigger_than_string
    """
    Why are there two expected results for this test?

    This Bite can be interpreted in two ways:

    1. A slice of size n moved from one end of the string to the other
    2. A continual rotation, character by character, n number of times

    Both interpretations result in identical output, except in the case
    where the rotation size exceeds the length of the string.

    Case 1) With a slice method, slicing an entire string and placing
    it at either the beginning or end of itself simply results in the
    the original string = expected_solution1

    Case 2) With a continual rotation, rotating the string len(string)
    number of times produces a string idential to the original string.
    This means any additional rotations can be considered equivalent to
    rotating the string by rotations % len(string) = expected_solution2
    """
    string = 'julian and bob!'
    expected_solution1 = 'julian and bob!'
    expected_solution2 = ' bob!julian and'
    ... rotate(string, 100) __ (expected_solution1,
                                   expected_solution2)

    mod = 100 % l..(string)  # 10
    ... rotate(string, mod) __ (expected_solution1,
                                   expected_solution2)