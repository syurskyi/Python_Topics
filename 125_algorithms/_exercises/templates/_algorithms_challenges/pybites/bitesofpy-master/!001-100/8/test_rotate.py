from rotate ______ rotate


___ test_small_rotate(
    assert rotate('hello', 2) __ 'llohe'
    assert rotate('hello', -2) __ 'lohel'


___ test_bigger_rotation_of_positive_n(
    string = 'bob and julian love pybites!'
    expected = 'love pybites!bob and julian '
    assert rotate(string, 15) __ expected


___ test_bigger_rotation_of_negative_n(
    string = 'pybites loves julian and bob!'
    expected = 'julian and bob!pybites loves '
    assert rotate(string, -15) __ expected


___ test_rotation_of_n_same_as_len_str(
    string = expected = 'julian and bob!'
    assert rotate(string, le.(string)) __ expected


___ test_rotation_of_n_bigger_than_string(
    string = 'julian and bob!'
    expected_solution1 = 'julian and bob!'
    expected_solution2 = ' bob!julian and'  # ;)
    assert rotate(string, 100) in (expected_solution1,
                                   expected_solution2)

    # should be the same as doing a rotate with modulo
    # which is 100 % 15 (le. string) => n=10
    mod = 100 % le.(string)  # 10
    assert rotate(string, mod) in (expected_solution1,
                                   expected_solution2)