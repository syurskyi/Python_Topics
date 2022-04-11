# _______ p__
#
# ____ ? _______ ?
#
#
# ?p__.m__.p. "arg, expected", [
#     ('upper', 'Mon, Thu'),
#     ('lower', 'Tue, Fri'),
#     ('30', 'Wed'),
#     ('30 min', 'Wed'),
#     ('30 min cardio', 'Wed'),
#     ('30 MIN CARDIO', 'Wed'),
#     ('upper body #1', 'Mon'),
#     ('upper body #2', 'Thu'),
#     ('lower body #1', 'Tue'),
#     ('lower body #2', 'Fri'),
#     ('Upper', 'Mon, Thu'),
#     ('UPPEr', 'Mon, Thu'),
#     ('Upper Body #', 'Mon, Thu'),
#     ('lower upper body', 'No matching workout'),
#     ('sun', 'No matching workout'),
#     ('30 min cardio -', 'No matching workout'),
#     ('nonsense', 'No matching workout'),
#
# ___ test_print_workout_days arg e.. capfd
#     ? ?
#     a..  ?.r .. 0 .s..
#     ... a.. __ e..