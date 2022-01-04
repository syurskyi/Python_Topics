_______ p__

____ workouts _______ print_workout_days


@p__.mark.parametrize(
        "arg, expected",[('upper','Mon, Thu\n'),('#1','Mon, Tue\n'),('lower','Tue, Fri\n'),('#2','Thu, Fri\n'),('thigh','No matching workout\n'),('LOWER','Tue, Fri\n')])
___ test_print_workout_days(arg,expected,capsys):
    result = print_workout_days(arg)
    captured = capsys.readouterr()
    ... captured.out __ expected

