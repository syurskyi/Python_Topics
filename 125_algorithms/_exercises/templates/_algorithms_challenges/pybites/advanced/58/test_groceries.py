# _______ p__
#
# ____ ? _______ ? ? ? ?
#
#
# ?p__.f..
# ___ cart
#     # faking some data (normally would load from DB)
#     products 'celery apples water coffee chicken pizza'.s..
#     prices [1, 4, 2, 5, 6, 4]
#     cravings F.., F.., F.., F.., F.., T..
#
#     items    # list
#     ___ item __ z.. ? ? ?
#         ?.a.. ? *?
#
#     r.. ? ?
#
#
# ?p__.f..
# ___ parser
#     r.. ?
#
#
# ___ test_list parser, cart, capfd
#     args p__..p..  '-l'
#     h.. a.. c..
#     output ?.r .. 0 .s..('\n')
#     ... 'pizza (craving)                |   4' __ output
#     ... 'Total                          |  22' __ output
#
#
# ___ test_search parser, cart, capfd
#     args p__..p..  '-s', 'coffee'
#     h.. a.. c..
#     output ?.r .. 0 .s.. '\n'
#     ... 'coffee                         |   5' __ output
#     ... 'Total                          |   5' __ output
#
#
# ___ test_add parser cart
#     ... l.. c.. __ 6
#     ... c__.d.. __ 22
#
#     args p__..p..  '-a', 'honey', '5', 'False'
#     handle_args a.. c..
#
#     ... l.. c.. __ 7
#     ... c__.d.. __ 27
#
#     new_item c.. -1
#     ... ?.p.. __ 'honey'
#     ... ?.p.. __ 5
#     ... n.. ?.c..
#
#
# ___ test_delete parser cart
#     # nice: fixture gives me a clean slate each test!
#     ... l.. c.. __ 6
#     ... c__.d.. __ 22
#
#     args p__..p..  '-d', 'pizza'
#     h.. a.. c..
#
#     ... l.. c.. __ 5
#     ... c__.d.. __ 18
#
#     new_last_item c.. -1
#     ... ?.p.. __ 'chicken'
#     ... ?.p.. __ 6
#     ... n.. ?.c..
#
#
# ___ test_args_mulually_exclusive parser
#     # argument -l/--list: not allowed with argument -d/--delete
#     w__ p__.r.. S..
#         p__..p..  '-d', 'pizza', '-l'
#
#     # argument -a/--add: expected 3 arguments
#     w__ p__.r.. S..
#         p__..p..  '-a', 'pizza'
#
#     # unrecognized arguments: coffee
#     w__ p__.r.. S..
#         p__..p..  '-d', 'pizza', 'coffee'