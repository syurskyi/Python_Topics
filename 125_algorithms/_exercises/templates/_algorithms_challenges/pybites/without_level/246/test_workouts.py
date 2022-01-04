_______ p__

____ workouts _______ print_workout_days


@p__.mark.parametrize('arg,expected',
                         [('upper', 'Mon, Thu\n'),
                          ('lower', 'Tue, Fri\n'),
                          ('cardio', 'Wed\n'),
                          ('glutes', 'No matching workout\n')])
___ test_print_workout_days(capsys, arg, expected):
    print_workout_days(arg)
    ... capsys.readouterr().out __ expected
