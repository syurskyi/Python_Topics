import pytest

from workouts import print_workout_days


@pytest.mark.parametrize(
        "arg, expected",[('upper','Mon, Thu\n'),('#1','Mon, Tue\n'),('lower','Tue, Fri\n'),('#2','Thu, Fri\n'),('thigh','No matching workout\n'),('LOWER','Tue, Fri\n')])
___ test_print_workout_days(arg,expected,capsys):
    result = print_workout_days(arg)
    captured = capsys.readouterr()
    assert captured.out == expected

