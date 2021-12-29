import pytest

from workouts import print_workout_days

@pytest.mark.parametrize("arg, expected", [
    ('#', 'Mon, Tue, Thu, Fri\n'), 
    ('30', 'Wed\n'), 
    ('30 min', 'Wed\n'), 
    ('cardio', 'Wed\n'), 
    ('#1', 'Mon, Tue\n'),
    ('#2', 'Thu, Fri\n'),
    ('upper', 'Mon, Thu\n'),
    ('lower', 'Tue, Fri\n'),
    ('body', 'Mon, Tue, Thu, Fri\n'),
    ('khoo', 'No matching workout\n')
])
def test_print_workout_days(capfd, arg, expected):
    print_workout_days(arg)
    output = capfd.readouterr()[0]
    assert output == expected