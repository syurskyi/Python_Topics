import pytest

from profile import get_profile


___ test_get_profile_no_name():
    with pytest.raises(TypeError):
        assert get_profile()


___ test_get_profile_no_age():
    with pytest.raises(TypeError):
        assert get_profile('tim')


___ test_get_profile_valueerror():
    with pytest.raises(ValueError):
        assert get_profile('tim', 'nonint')


___ test_get_profile_too_many_sports():
    with pytest.raises(ValueError):
        sports = ['tennis', 'basketball', 'badminton',
                  'baseball', 'volleyball', 'boxing']
        assert get_profile('tim', 36, *sports)


___ test_get_profile_dict():
    assert get_profile('tim', 36) == {'name': 'tim', 'age': 36}


___ test_get_profile_one_sport():
    expected = {'name': 'tim', 'age': 36,
                'sports': ['tennis']}
    assert get_profile('tim', 36, 'tennis') == expected


___ test_get_profile_two_sports():
    expected = {'name': 'tim', 'age': 36,
                'sports': ['basketball', 'tennis']}
    assert get_profile('tim', 36, 'tennis', 'basketball') == expected


___ test_get_profile_award():
    expected = {'name': 'tim', 'age': 36,
                'awards': {'champ': 'helped out team in crisis'}}
    assert get_profile('tim', 36,
                       champ='helped out team in crisis') == expected


___ test_get_profile_two_sports_and_one_award():
    expected = {'name': 'tim', 'age': 36,
                'sports': ['basketball', 'tennis'],
                'awards': {'champ': 'helped out team in crisis'}}
    assert get_profile('tim', 36, 'tennis', 'basketball',
                       champ='helped out team in crisis') == expected


___ test_get_profile_two_sports_and_three_awards():
    expected = {'name': 'tim', 'age': 36,
                'sports': ['basketball', 'tennis'],
                'awards': {'champ': 'helped out the team in crisis',
                           'service': 'going the extra mile for our customers',
                           'attitude': 'unbeatable positive + uplifting'}}
    assert get_profile('tim', 36, 'tennis', 'basketball',
                       service='going the extra mile for our customers',
                       champ='helped out the team in crisis',
                       attitude='unbeatable positive + uplifting') == expected