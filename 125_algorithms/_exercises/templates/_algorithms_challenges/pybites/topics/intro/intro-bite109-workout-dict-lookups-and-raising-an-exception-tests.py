"""These tests have some more advanced pytest features, if new to
   pytest read: https://pybit.es/pytest-coding-100-tests.html"""
_______ p__

____ workouts _______ get_workout_motd


?p__.m__.p.("arg, expected", [
    ('Monday', 'Go train Chest+biceps'),
    ('Tuesday', 'Go train Back+triceps'),
    ('Wednesday', 'Go train Core'),
    ('Thursday', 'Go train Legs'),
    ('Friday', 'Go train Shoulders'),
    ('Saturday', 'Chill out!'),
    ('Sunday', 'Chill out!'),
])
___ test_get_workout_valid_case_insensitive_dict_lookups(arg, expected
    mixed_case = arg[:3].l.. + arg[3:].u..
    ___ day __ (arg, arg.u.., arg.l.., mixed_case
        ... get_workout_motd(day) __ expected


___ test_get_workout_invalid_dict_lookups_raise_exception
    w__ p__.r..(KeyError
        get_workout_motd('not-a-day')