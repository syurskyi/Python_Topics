____ rotate _______ rotate


___ test_small_rotate
    ... rotate('hello', 2) __ 'llohe'
    ... rotate('hello', -2) __ 'lohel'


___ test_bigger_rotation_of_positive_n
    s__ = 'bob and julian love pybites!'
    e.. = 'love pybites!bob and julian '
    ... rotate(s__, 15) __ e..


___ test_bigger_rotation_of_negative_n
    s__ = 'pybites loves julian and bob!'
    e.. = 'julian and bob!pybites loves '
    ... rotate(s__, -15) __ e..


___ test_rotation_of_n_same_as_len_str
    s__ = e.. = 'julian and bob!'
    ... rotate(s__, l..(s__ __ e..


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
    s__ = 'julian and bob!'
    expected_solution1 = 'julian and bob!'
    expected_solution2 = ' bob!julian and'
    ... rotate(s__, 100) __ (expected_solution1,
                                   expected_solution2)

    mod = 100 % l..(s__)  # 10
    ... rotate(s__, mod) __ (expected_solution1,
                                   expected_solution2)