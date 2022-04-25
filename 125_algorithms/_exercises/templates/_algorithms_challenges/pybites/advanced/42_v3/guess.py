# _______ r__
#
# MAX_GUESSES 5
# START, END 1, 20
#
#
# ___ get_random_number
#     """Get a random number between START and END, returns int"""
#     r.. r__.r.. ? ?
#
#
# c_ Game
#     """Number guess class, make it callable to initiate game"""
#
#     ___ -
#         """Init _guesses, _answer, _win to set(), get_random_number(), False"""
#         _guesses s..
#         _answer ?
#         _win F..
#
#     ___ guess
#         """Ask user for input, convert to int, raise ValueError outputting
#            the following errors when applicable:
#            'Please enter a number'
#            'Should be a number'
#            'Number not in range'
#            'Already guessed'
#            If all good, return the int"""
#         ? i.. 'Your guess: '
#         __ n.. ?
#             print 'Please enter a number'
#             r.. V... 'Nothing entered'
#         __ n.. a.. c.i.. ___ ? __ s.. ?
#             print 'Should be a number'
#             r.. V... 'Non-digit entered'
#         guess i.. ?
#         __ n..  S.. <_ ? <_ ?
#             print 'Number not in range'
#             r.. V... 'Out of range'
#         __ ? __ _?
#             print 'Already guessed'
#             r.. V... 'Retry previous guess'
#         _?.a.. ?
#         r.. ?
#
#     ___ _validate_guess  guess
#         """Verify if guess is correct, print the following when applicable:
#            {guess} is correct!
#            {guess} is too low
#            {guess} is too high
#            Return a boolean"""
#         __ ? __ _?
#             print _* ? is correct!
#             r.. T..
#         ____ ? < _?
#             print _* ? is too low
#         ____
#             print _* ? is too high
#         r.. F..
#
#     ___ -c
#         """Entry point / game loop, use a loop break/continue,
#            see the tests for the exact win/lose messaging"""
#         w.... l.. _? < M.. a.. n.. _?
#             ___
#                 this_guess g..
#             ______ V..
#                 _____
#             __ _? ?
#                 _? T..
#                 r..
#         print _*Guessed M.. times, answer was _?
#         r..
#
#
# __ _____ __ _____
#     game ?
#     ?
