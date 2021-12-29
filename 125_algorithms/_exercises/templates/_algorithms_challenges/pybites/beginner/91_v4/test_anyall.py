_______ pytest

____ Previous.anyall _______ (contains_only_vowels,
                             contains_any_py_chars,
                             contains_digits)


@pytest.mark.parametrize("arg, expected", [
    ('aioue', True),
    ('EoUia', True),
    ('aaAiIee', True),
    ('AEIOU', True),
    ('aaeeouu', True),
    ('abcde', False),
    ('AE123', False),
    ('AiOuef', False),
])
___ test_contains_only_vowels(arg, expected):
    ... bool(contains_only_vowels(arg)) __ expected


@pytest.mark.parametrize("arg, expected", [
    ('Python', True),
    ('pycharm', True),
    ('PYTHON', True),
    ('teaser', True),
    ('bob', True),
    ('julian', True),
    ('yes', True),
    ('no', True),
    ('america', False),
    ('B@b', False),
    ('Jules', False),
    ('agua', False),
    ('123', False),
    ('', False),
])
___ test_contains_any_py_chars(arg, expected):
    ... bool(contains_any_py_chars(arg)) __ expected


@pytest.mark.parametrize("arg, expected", [
    ('yes1', True),
    ('123', True),
    ('hello2', True),
    ('up2date', True),
    ('yes', False),
    ('hello', False),
    ('', False),
])
___ test_contains_digits(arg, expected):
    ... bool(contains_digits(arg)) __ expected