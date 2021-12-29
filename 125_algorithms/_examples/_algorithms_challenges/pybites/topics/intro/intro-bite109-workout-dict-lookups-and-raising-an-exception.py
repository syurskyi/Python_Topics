import string
'''
Bite 109. Workout dict lookups and raising an exception
In this Bite you learn how to lookup values from a dictionary or in Python: dict.

You are presented with workout_schedule with keys: days and values: workouts.
Complete get_workout_motd that receives a day string, title case it so the function can receive case insensitive days,
look it up in the dict and do two things:

If the day (key) is not in the dictionary, raise a KeyError, we don't want this function to continue,
the caller needs to catch this exception,
If the key is in the dictionary, return chill or go_train depending if it's a Rest day or not.
The latter you will need to string-interpolate using format.
'''

'''
bite attempted on 20/06/2019

Notes:

* capitalize() vs title()
* https://www.thoughtco.com/pythons-string-templates-2813675

- capitalize() will only capitalize the first character if it's a letter
- title() will capitalize the first letter encountered, with a weird issue capitalizing every letter 
encountered after an apostrophe

'''

workout_schedule = {'Friday': 'Shoulders',
                    'Monday': 'Chest+biceps',
                    'Saturday': 'Rest',
                    'Sunday': 'Rest',
                    'Thursday': 'Legs',
                    'Tuesday': 'Back+triceps',
                    'Wednesday': 'Core'}
rest, chill, go_train = 'Rest', 'Chill out!', 'Go train {}'

def get_workout_motd(day):
    """Title case passed in day argument (monday or MONDAY -> Monday)
       and check if it is in the given workout_schedule dict.

       If it is there retrieve the workout, if not raise a KeyError.

       Return the chill or go_train variable depending the retrieved
       workout value ('Rest' or workout bla)

       Trivia: /etc/motd is a file on Unix-like systems that contains
       a 'message of the day'"""
    d = day.capitalize()
    work = workout_schedule[d]
    if work == "Rest":
        return chill
    else:
        return f"Go train {work}"



print(get_workout_motd("monday"))