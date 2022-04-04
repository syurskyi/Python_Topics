_______ p__

____ workouts _______ print_workout_days


?p__.m__.p.('arg,expected',
                         [('upper', 'Mon, Thu\n'),
                          ('lower', 'Tue, Fri\n'),
                          ('cardio', 'Wed\n'),
                          ('glutes', 'No matching workout\n')])
___ test_print_workout_days(capsys, arg, e..
    print_workout_days(arg)
    ... capsys.readouterr().out __ e..
