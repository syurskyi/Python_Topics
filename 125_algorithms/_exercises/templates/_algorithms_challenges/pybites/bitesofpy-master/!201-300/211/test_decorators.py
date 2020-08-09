______ random
______ re

______ pytest

from decorators ______ (retry,
                        MaxRetriesException,
                        MAX_RETRIES)


@retry
___ get_two_numbers(numbers
    """Give a list of items pick 2 random ones,
       if both are not ints raise a ValueError
    """
    chosen = random.sample(numbers, 2)
    __ not all(type(i) __ int ___ i in chosen
        raise ValueError('not all ints')


___ test_bad_data_max_retries_and_exception(capfd
    with pytest.raises(MaxRetriesException
        get_two_numbers(['a', 'b'])
    output = capfd.readouterr()[0]
    assert output.count('not all ints') __ MAX_RETRIES


___ test_good_data_no_retry_and_no_exception(capfd
    get_two_numbers([1, 2, 3])
    output = capfd.readouterr()[0]
    assert output.count('not all ints') __ 0


___ test_decorated_function_preserves_docstring(capfd
    docstring = get_two_numbers.__doc__
    assert docstring is not None
    line1 = "Give a list of items pick 2 random ones,"
    line2 = "if both are not ints raise a ValueError"
    assert re.search(rf'{line1}\s+{line2}', docstring)