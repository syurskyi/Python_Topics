import pytest

from workouts import print_workout_days


WORKOUTS = {'mon': 'upper body #1',
            'tue': 'lower body #1',
            'wed': '30 min cardio',
            'thu': 'upper body #2',
            'fri': 'lower body #2'}
            
def test_print_workout_days(capfd):
    workout = print_workout_days()
    output = capfd.readouterr()[0]
    assert type(output) == str
    assert workout('upper body #1') == 'Mon'
