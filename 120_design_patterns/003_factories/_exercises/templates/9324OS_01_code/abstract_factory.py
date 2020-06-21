# c_ Frog
#     ___ - name
#         ?  ?
#
#     ___ -s
#         r_ n..
#
#     ___ interact_with obstacle
#         print('@ the Frog encounters @ and @!'.f..  ? ?.a..
#
# c_ Bug
#     ___ -s
#         r_ 'a bug'
#
#     ___ action
#         r_ 'eats it'
#
# c_ FrogWorld
#     ___ - name
#         print
#         player_name _ ?
#
#     ___ -s
#         r_ '\n\n\t------ Frog World -------'
#
#     ___ make_character
#         r_ F.. p_n..
#
#     ___ make_obstacle
#         r_ B..
#
# c_ Wizard
#     ___ - name
#         ?  ?
#
#     ___ -s
#         r_ n..
#
#     ___ interact_with obstacle
#         print('@ the Wizard battles against @ and @!'.f..  ?  ?.a..
#
# c_ Ork
#     ___ -s
#         r_ 'an evil ork'
#
#     ___ action
#         r_ 'kills it'
#
# c_ WizardWorld
#     ___ - name
#         print
#         player_name _ ?
#
#     ___ -s
#         r_ '\n\n\t------ Wizard World -------'
#
#     ___ make_character
#         r_ W.. p_n..
#
#     ___ make_obstacle
#         r_ O..
#
# c_ GameEnvironment
#     ___ - factory
#         ?hero _ ?.m_c..
#         ?obstacle _ ?.m_o..
#
#     ___ play
#         ?h__.i_w.. ?o..
#
# ___ main
#     name = i.. "Hello. What's your name? "
#     valid_input = F..
#     w___ no. ?
#         ___
#             age = in.. ('Welcome @. How old are you? '.f.. n..
#             age = in. ?
#             valid_input = T..
#             game = FW.. __ a.. < 18 ____ WiW..
#             environment = GE.. g.. n..
#             ?.p..
#         _______ V... __ err:
#             print("Age @ is invalid, please try again...".f.. a..
#
# __ _______ __ _____
#     ?
