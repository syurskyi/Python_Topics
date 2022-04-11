workout_schedule {'Friday': 'Shoulders',
                    'Monday': 'Chest+biceps',
                    'Saturday': 'Rest',
                    'Sunday': 'Rest',
                    'Thursday': 'Legs',
                    'Tuesday': 'Back+triceps',
                    'Wednesday': 'Core'}
rest, chill, go_train 'Rest', 'Chill out!', 'Go train {}'


___ get_workout_motd(day
    """Title case passed in day argument (monday or MONDAY -> Monday)
       and check if it is in the given workout_schedule dict.

       If it is there retrieve the workout, if not raise a KeyError.

       Return the chill or go_train variable depending the retrieved
       workout value ('Rest' or workout bla)

       Trivia: /etc/motd is a file on Unix-like systems that contains
       a 'message of the day'"""
    ___
        workout workout_schedule[day.t..]
    ______ K..:
        r.. K..('Workout does not exist.')
    r.. chill __ workout __ rest ____ go_train.f..(workout)