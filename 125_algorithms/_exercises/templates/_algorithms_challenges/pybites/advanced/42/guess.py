# _______ r__
# MAX_GUESSES 5
# START, END 1, 20
#
#
# ___ get_random_number
#     """Get a random number between START and END, returns int"""
#     r.. r__.r.. ?
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
#
#
#
#
#     ___ guess
#         """Ask user for input, convert to int, raise ValueError outputting
#            the following errors when applicable:
#            'Please enter a number'
#            'Should be a number'
#            'Number not in range'
#            'Already guessed'
#            If all good, return the int"""
#
#         w... T...
#             ___
#                 number i.. "Guess a number between 1 and 20: ")
#                 result i.. ?
#             ______:
#                 __ ? __ N.. o. l.. ? __ 0
#                     print('Please enter a number')
#                 ____
#                     print('Should be a number')
#                 r.. V...
#             ____
#                 __ n.. ? <_ ? <_ ?
#                     print('Number not in range')
#                 ____ ? __ _?
#                     print('Already guessed')
#                 ____
#                     _?.a.. ?
#                     r.. ?
#                 r.. V...
#
#
#
#
#
#
#
#
#
#     ___ _validate_guess  guess
#         """Verify if guess is correct, print the following when applicable:
#            {guess} is correct!
#            {guess} is too low
#            {guess} is too high
#            Return a boolean"""
#
#         correct F..
#         __ ? __ _answer
#             print _*? is correct!
#             ? T..
#         ____ ? > _?
#             print _*? is too high
#         ____
#             print _*? is too low
#
#         r.. ?
#     ___ -c
#         """Entry point / game loop, use a loop break/continue,
#            see the tests for the exact win/lose messaging"""
#
#
#         ___ i __ r.. 1 M.. + 1
#             w... T...
#                 ___
#                     user_guess ?
#                 ______ V..
#                     p..
#                 ____
#                     _____
#
#
#             _win _v.. u..
#
#
#             __ ?
#                 _____
#
#
#         __ ?
#             print _*It took you ? guesses
#         ____
#             print _*Guessed 5 times, answer was ?
#
#
#
#
#
#
#
#
#
#
#
# __ _____ __ _____
#     game ?
#     g?
