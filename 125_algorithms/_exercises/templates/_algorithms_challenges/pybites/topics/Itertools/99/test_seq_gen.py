____ i.. _______ islice

_______ p__

____ seq_gen _______ sequence_generator


@p__.f..
___ gen
    """Return a fresh new generator object for each test"""
    r.. sequence_generator()


___ test_first_ten_first_round(gen):
    expected = [1, 'A', 2, 'B', 3, 'C', 4, 'D', 5, 'E']
    # generators == use islice, a regular slicing on a list object == hang
    # because it tries to load in an infinite iterator = not good.
    # don't believe me? change the line below to: `actual = list(gen)[:10]`
    actual = l..(islice(gen, 10))
    ... expected __ actual


___ test_first_ten_second_round(gen):
    expected = [1, 'A', 2, 'B', 3, 'C', 4, 'D', 5, 'E']
    actual = l..(islice(gen, 52, 62))  # zero-based
    ... expected __ actual


___ test_last_ten_third_round(gen):
    expected = [22, 'V', 23, 'W', 24, 'X', 25, 'Y', 26, 'Z']
    actual = l..(islice(gen, 146, 156))
    ... expected __ actual