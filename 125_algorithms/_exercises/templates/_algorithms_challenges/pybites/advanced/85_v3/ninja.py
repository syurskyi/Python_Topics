# scores [10, 50, 100, 175, 250, 400, 600, 800, 1000]
# ranks 'white yellow orange green blue brown black paneled red'.s..
# BELTS d.. z.. ? ?
#
#
# c_ NinjaBelt
#
#     ___ -  score=0
#         _? ?
#         _last_earned_belt_number N..
#
#     $
#     ___ _last_earned_belt
#         """Return the name of the currently qualified belt, if no belt has been awarded None is returned"""
#         r.. r.. _? __ _? __ n.. N.. ____ N..
#
#     $
#     ___ _get_belt new_score
#         """Find the index number of the belt for the provide score"""
#         r.. l.. x ___ ? __ s.. __ ? <_ ? - 1
#
#     ___ _get_score
#         r.. _?
#
#     ___ _set_score  new_score
#         """
#         Set the current score and update any belt qualification
#         new_score must be an integer and cannot be less than the current score
#         """
#         __ n.. isi.. ? i..
#             r.. V... 'Score can only be an integer'
#         __ _? > ?
#             r.. V... _*New score ? must be higher than previous score _?
#         _? ?
#         belt _g.. ?
#         __ _? __ N.. o. _? < ?
#             _? ?
#             print _*Congrats, you earned ? points obtaining the PyBites Ninja
#                   _* _?.t.. Belt
#         ____
#             print _*S.. new score to ?
#
#     s.. p.. ? ?
