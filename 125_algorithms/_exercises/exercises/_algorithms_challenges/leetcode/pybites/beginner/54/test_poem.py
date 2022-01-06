# ____ p.. _______ p..
#
# # part of William Shakespeare's play Hamlet
# shakespeare_unformatted = """
#                           To be, or not to be, that is the question:
#                           Whether 'tis nobler in the mind to suffer
#
#                           The slings and arrows of outrageous fortune,
#                           Or to take Arms against a Sea of troubles,
#                           """
#
# shakespeare_formatted = """
# To be, or not to be, that is the question:
#     Whether 'tis nobler in the mind to suffer
# The slings and arrows of outrageous fortune,
#     Or to take Arms against a Sea of troubles,
# """
#
# # part of Remember, by Christina Rosetti
# rosetti_unformatted = """
#                       Remember me when I am gone away,
#                       Gone far away into the silent land;
#                       When you can no more hold me by the hand,
#
#                       Nor I half turn to go yet turning stay.
#
#                       Remember me when no more day by day
#                       You tell me of our future that you planned:
#                       Only remember me; you understand
#                       """
#
#
# rosetti_formatted = """
# Remember me when I am gone away,
#     Gone far away into the silent land;
#     When you can no more hold me by the hand,
# Nor I half turn to go yet turning stay.
# Remember me when no more day by day
#     You tell me of our future that you planned:
#     Only remember me; you understand
# """
#
#
# ___ test_shakespeare_text capfd
#     ? ?
#     output  ?.r.. 0
#     ... ?.s.. __ ?.s..
#
#
# ___ test_rosetti_poem capfd
#     ? ?
#     output  ?.r.. 0
#     ... ?.s.. __ ?.s..
