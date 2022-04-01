_______ p__

____ Previous.anyall _______ (contains_only_vowels,
                             contains_any_py_chars,
                             contains_digits)


@p__.m__.p..("arg, expected", [
    ('aioue', T..),
    ('EoUia', T..),
    ('aaAiIee', T..),
    ('AEIOU', T..),
    ('aaeeouu', T..),
    ('abcde', F..),
    ('AE123', F..),
    ('AiOuef', F..),
])
___ test_contains_only_vowels(arg, expected):
    ... bool(contains_only_vowels(arg)) __ expected


@p__.m__.p..("arg, expected", [
    ('Python', T..),
    ('pycharm', T..),
    ('PYTHON', T..),
    ('teaser', T..),
    ('bob', T..),
    ('julian', T..),
    ('yes', T..),
    ('no', T..),
    ('america', F..),
    ('B@b', F..),
    ('Jules', F..),
    ('agua', F..),
    ('123', F..),
    ('', F..),
])
___ test_contains_any_py_chars(arg, expected):
    ... bool(contains_any_py_chars(arg)) __ expected


@p__.m__.p..("arg, expected", [
    ('yes1', T..),
    ('123', T..),
    ('hello2', T..),
    ('up2date', T..),
    ('yes', F..),
    ('hello', F..),
    ('', F..),
])
___ test_contains_digits(arg, expected):
    ... bool(contains_digits(arg)) __ expected