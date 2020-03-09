# from pyparsing import Word, OneOrMore, Optional, Group, Suppress, alphanums
#
# c_ Gate
#     ___ -
#         is_open _ F..
#
#     ___ __str__
#         r_ *o.. __ is_open ____ *c..
#
#     ___ open
#         print('opening the gate')
#         i_o.. _ T..
#
#     ___ close
#         print('closing the gate')
#         i_o.. _ F..
#
# c_ Garage
#     ___ -
#         i_o.. _ F..
#
#     ___ __str__
#         r_ *o.. __ i_o.. ____ *c..
#
#     ___ open
#         print('opening the garage')
#         i_o.. _ T..
#
#     ___ close
#         print('closing the garage')
#         i_o.. _ F..
#
# c_ Aircondition:
#     ___ -
#         is_on _ F..
#
#     ___ -s
#         r_ 'on' __ is_on ____ 'off'
#
#     ___ turn_on
#         print('turning on the aircondition')
#         i_o. _ T..
#
#     ___ turn_off
#         print('turning off the aircondition')
#         i_o. _ F..
#
# c_ Heating:
#     ___ -
#         is_on _ F..
#
#     ___ -s
#         r_ 'on' __ is_on ____ 'off'
#
#     ___ turn_on
#         print('turning on the heating')
#         i_o. _ T..
#
#     ___ turn_off
#         print('turning off the heating')
#         i_o. _ F..
#
# c_ Boiler
#     ___ -
#         temperature _ 83 # __ celsius
#
#     ___ -s
#         r_ 'boiler temperature: @'.f.. ?
#
#     ___ increase_temperature amount
#         print("increasing the boiler's temperature by @ degrees".f.. ?
#         t.. +_ a..
#
#     ___ decrease_temperature amount
#         print("decreasing the boiler's temperature by @ degrees".f.. /
#         t.. -_ ?
#
# c_ Fridge
#     ___ -
#         temperature _ 2 # __ celsius
#
#     ___ -s
#         r_ 'fridge temperature: @'.f.. ?
#
#     ___ increase_temperature amount
#         print("increasing the fridge's temperature by @ degrees".f.. ?
#         t.. +_ ?
#
#     ___ decrease_temperature, amount
#         print("decreasing the fridge's temperature by @ degrees".f.. ?
#         t.. -_ ?
#
#
# ___ mai
#     word _ W.. a_a..
#     command _ G.. OOM.. ?
#     token _ S.. ("->")
#     device _ G.. OOM.. w..
#     argument _ G.. OOM.. w..
#     event _ c.. + t.. + d.. + O.. t.. + a..
#
#     gate _ ?
#     garage _ ?
#     airco _ ?
#     heating _ ?
#     boiler _ ?
#     fridge _ ?
#
#     tests _ ('open -> gate',
#              'close -> garage',
#              'turn on -> aircondition',
#              'turn off -> heating',
#              'increase -> boiler temperature -> 5 degrees',
#              'decrease -> fridge temperature -> 2 degrees')
#
#     open_actions _ |*gate ?.o.. *garage ?.o.. *aircondition ?.t_o
#                   *heating ?.t_o. *boiler temperature ?.i_t..
#                   *fridge temperature ?.i_t..
#     close_actions _ |*gate ?.cl.. *garage ?.cl.. *aircondition a___.t_o..
#                    *heating ?.t_of. *boiler temperature ?.d_t..
#                    *fridge temperature ?.d_t..
#
#     ___ t __ tests
#         __ le. e___.pS.. t __ 2: # no argument
#             cmd, dev _ e___.pS.. t
#             cmd_str, dev_str _ ' '.jo.. c.. ' '.jo.. d..
#             __ *o.. __ c_s.. o. 'turn on' __ c_s..
#                 o_a..|d_s..
#             ____ *close __ cmd_str or *turn off __ c_s..
#                 c_a..|d_s..
#         ____ le. e___.pS.. t __ 3 # argument
#             cmd, dev, arg _ e___.pS.. t
#             cmd_str, dev_str, arg_str _ ' '.jo.. c.. ' '.jo.. d.. ' '.jo.. a..
#             num_arg _ 0
#             ___
#                 num_arg _ in.  a_s__.sp.. 0 # extract the numeric part
#             ______ V.. __ err
#                 print("expected number but got: '@'".f.. a_s.. 0
#             __ *increase __ c_s.. an n_a.. > 0
#                 o_a..|d_s.. n_a..
#             ____ *decrease  __ c_s.. an. n_a.. > 0
#                 c_a..|d_s..||n_a..
#
# __ _______ __ ______
#     ?
