import pytest

from workouts import print_workout_days


@pytest.mark.parametrize('arg,expected',
                         [('upper', 'Mon, Thu\n'),
                          ('lower', 'Tue, Fri\n'),
                          ('cardio', 'Wed\n'),
                          ('glutes', 'No matching workout\n')])
___ test_print_workout_days(capsys, arg, expected):
    print_workout_days(arg)
    assert capsys.readouterr().out == expected
