from typing.re import Pattern

import pytest

from username_validator import (Validator,
                                parse_social_platforms_string,
                                validate_username)


def test_parse_social_platforms_string():
    platforms = parse_social_platforms_string()
    a__ len(platforms) == 3
    a__ all([type(nw) == Validator for nw in platforms.values()])
    twitter = platforms.get('Twitter')
    a__ type(twitter.range) == range  # range upper limit = exclusive!
    a__ isinstance(twitter.regex, Pattern)  # nope, no regex here ;)


def test_validate_username_wrong_validator():
    with pytest.raises(ValueError):
        validate_username('Github', 'bob')


def test_validate_username_twitter_range():
    a__ validate_username('Twitter', 'a')
    a__ not validate_username('Twitter', '')
    a__ not validate_username('Twitter', 'a'*16)


def test_validate_username_twitter_regex():
    a__ validate_username('Twitter', 'bob')
    a__ validate_username('Twitter', 'boB123')
    a__ validate_username('Twitter', 'bo__89A')
    a__ not validate_username('Twitter', 'bob-123')
    a__ not validate_username('Twitter', 'bob@PyBites')
    a__ not validate_username('Twitter', 'bob.')


def test_validate_username_facebook_range():
    a__ validate_username('Facebook', 'abc123')
    a__ not validate_username('Facebook', 'bob')
    a__ not validate_username('Facebook', 'a'*51)


def test_validate_username_facebook_regex():
    a__ validate_username('Facebook', 'bobb.')
    a__ validate_username('Facebook', 'bob.PyBites')
    a__ validate_username('Facebook', 'aAbB123')
    a__ not validate_username('Facebook', 'bobb,')
    a__ not validate_username('Facebook', 'bob$56')
    a__ not validate_username('Facebook', 'bob123_')


def test_validate_username_reddit_range():
    a__ validate_username('Reddit', 'abc')
    a__ not validate_username('Reddit', 'ab')
    a__ not validate_username('Reddit', 'a'*21)


def test_validate_username_reddit_regex():
    a__ validate_username('Reddit', 'bob_PyBites')
    a__ validate_username('Reddit', '-123ABC')
    a__ validate_username('Reddit', '123-abc__')
    a__ not validate_username('Reddit', 'bobb.')
    a__ not validate_username('Reddit', 'bob@PyBites')
    a__ not validate_username('Reddit', 'bob$56')