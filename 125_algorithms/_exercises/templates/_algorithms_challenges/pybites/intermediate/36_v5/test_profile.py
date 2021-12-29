_______ pytest

____ profile _______ get_profile


___ test_get_profile_no_name():
    with pytest.raises(TypeError):
        ... get_profile()


___ test_get_profile_no_age():
    with pytest.raises(TypeError):
        ... get_profile('tim')


___ test_get_profile_valueerror():
    with pytest.raises(ValueError):
        ... get_profile('tim', 'nonint')


___ test_get_profile_too_many_sports():
    with pytest.raises(ValueError):
        sports = ['tennis', 'basketball', 'badminton',
                  'baseball', 'volleyball', 'boxing']
        ... get_profile('tim', 36, *sports)


___ test_get_profile_dict():
    ... get_profile('tim', 36) __ {'name': 'tim', 'age': 36}


___ test_get_profile_one_sport():
    expected = {'name': 'tim', 'age': 36,
                'sports': ['tennis']}
    ... get_profile('tim', 36, 'tennis') __ expected


___ test_get_profile_two_sports():
    expected = {'name': 'tim', 'age': 36,
                'sports': ['basketball', 'tennis']}
    ... get_profile('tim', 36, 'tennis', 'basketball') __ expected


___ test_get_profile_award():
    expected = {'name': 'tim', 'age': 36,
                'awards': {'champ': 'helped out team in crisis'}}
    ... get_profile('tim', 36,
                       champ='helped out team in crisis') __ expected


___ test_get_profile_two_sports_and_one_award():
    expected = {'name': 'tim', 'age': 36,
                'sports': ['basketball', 'tennis'],
                'awards': {'champ': 'helped out team in crisis'}}
    ... get_profile('tim', 36, 'tennis', 'basketball',
                       champ='helped out team in crisis') __ expected


___ test_get_profile_two_sports_and_three_awards():
    expected = {'name': 'tim', 'age': 36,
                'sports': ['basketball', 'tennis'],
                'awards': {'champ': 'helped out the team in crisis',
                           'service': 'going the extra mile for our customers',
                           'attitude': 'unbeatable positive + uplifting'}}
    ... get_profile('tim', 36, 'tennis', 'basketball',
                       service='going the extra mile for our customers',
                       champ='helped out the team in crisis',
                       attitude='unbeatable positive + uplifting') __ expected