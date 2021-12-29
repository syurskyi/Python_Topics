WORKOUTS = {'mon': 'upper body #1',
            'tue': 'lower body #1',
            'wed': '30 min cardio',
            'thu': 'upper body #2',
            'fri': 'lower body #2'}

___ print_workout_days(workout: str, my_workouts: dict = WORKOUTS) -> None:
    """Print the days (comma separated and title cased) of my_workouts
       that (partially) match the workout string passed in. If no
       workout matches, print 'No matching workout'
    """
    days = [day.title() for day, wo in my_workouts.items()
            __ workout.lower() in wo.lower()]
    print(', '.join(days) __ days else 'No matching workout')
