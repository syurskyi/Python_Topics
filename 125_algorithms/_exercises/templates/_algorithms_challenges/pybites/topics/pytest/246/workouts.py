WORKOUTS = {'mon': 'upper body #1',
            'tue': 'lower body #1',
            'wed': '30 min cardio',
            'thu': 'upper body #2',
            'fri': 'lower body #2'}


___ print_workout_days(workout: s.., my_workouts: d.. = WORKOUTS) __ N..
    """Print the days (comma separated and title cased) of my_workouts
       that (partially) match the workout string passed in. If no
       workout matches, print 'No matching workout'
    """
    days = [day.t.. ___ day, wo __ my_workouts.i..
            __ workout.l.. __ wo.l..]
    print(', '.j..(days) __ days ____ 'No matching workout')

print_workout_days('lower')