_______ pytest

____ workouts _______ print_workout_days


WORKOUTS = {'mon': 'upper body #1',
            'tue': 'lower body #1',
            'wed': '30 min cardio',
            'thu': 'upper body #2',
            'fri': 'lower body #2'}
            
___ test_print_workout_days(capfd):
    output = capfd.readouterr()[0]
    print(output)
    ... type(output) __ s..
    ... print_workout_days('upper body #1') __ 'Mon'
