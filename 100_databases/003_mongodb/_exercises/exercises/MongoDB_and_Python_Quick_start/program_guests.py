# ______ d_t_
# ____ dateutil ______ pa..
#
# ____ i__.s.. ______ sw..
# ______ p_h.. __ h..
# ______ s__.data_service __ svc
# ____ p_h.. ______ su_m.. e_m..
# ______ i_.s.. __ s..
#
#
# ___ r..
#     print(' ****************** Welcome guest **************** ')
#     print()
#
#     s_c..
#
#     w__ T..
#         action _ h__.g_a..
#
#         w__ s.. ? __ s
#             ?.c.. 'c', h__.c_a_
#             ?.c.. 'l', h__.l_i_a..
#
#             ?.c.. 'a', a..
#             ?.c.. 'y', v..
#             ?.c.. 'b', b..
#             ?.c.. 'v', v..
#             ?.c.. 'm', l___ 'change_mode')
#
#             ?.c.. '?' s_c..
#             ?.c.. '', l___ N..)
#             ?.c..  'x', 'bye', 'exit', 'exit()' h__.e_a..
#
#             ?.d.. h__.u..
#
#         s__.r_a..
#
#         __ action
#             print()
#
#         __ ?.r.. __ 'change_mode'
#             r_
#
#
# ___ show_commands
#     print('What action would you like to take:')
#     print('[C]reate an account')
#     print('[L]ogin to your account')
#     print('[B]ook a cage')
#     print('[A]dd a snake')
#     print('View [y]our snakes')
#     print('[V]iew your bookings')
#     print('[M]ain menu')
#     print('e[X]it app')
#     print('[?] Help (this info)')
#     print()
#
#
# ___ add_a_snake
#     print(' ****************** Add a snake **************** ')
#     __ no. s__.a_a..
#         error_msg("You must log in first to add a snake")
#         r_
#
#     name _ in.. "What is your snake's name? "
#     __ no. ?
#         e_m.. 'cancelled'
#         r_
#
#     length _ fl.. in.. 'How long is your snake (in meters)? '
#     species _ in..("Species? ")
#     is_venomous _ in.. "Is your snake venomous [y]es, [n]o? ").l.. .s_w.. 'y')
#
#     snake _ s__.a_s.. s__.a_a.. n.. l.. s.. i_v..
#     s__.r_a..
#     success_msg('Created {} with id {}'.f.. s__.n.. s__.i.
#
#
# ___ view_your_snakes
#     print(' ****************** Your snakes **************** ')
#     __ no. s__.a_a..
#         e_m..("You must log in first to view your snakes")
#         r_
#
#     snakes _ s__.g_sn_f_u.. s__.a_a...id
#     print("You have @ snakes.".f.. le. ?
#     ___ s __ snakes:
#         print(" * @ is a @ that is @m long and is @venomous.".f..(
#             ?.n..
#             ?.s..
#             ?.l..
#             '' __ ?.i.. ____ 'not '
#         ))
#
#
# ___ book_a_cage
#     print(' ****************** Book a cage **************** ')
#     __ no. s__.a_a..
#         e_m..("You must log in first to book a cage")
#         r_
#
#     snakes _ s__.g_s_f_u.. s__.a_a...id
#     __ no. ?
#         e_m.. 'You must first [a]dd a snake before you can book a cage.'
#         r_
#
#     print("Let's start by finding available cages.")
#     start_text _ in.. "Check-in date [yyyy-mm-dd]: "
#     __ no. ?
#         e_m.. 'cancelled'
#         r_
#
#     checkin _ p__.p..
#         s_t..
#
#     checkout _ p__.p..
#         in.. "Check-out date [yyyy-mm-dd]: "
#
#     __ c.. >_ c..
#         e_m('Check in must be before check out')
#         r_
#
#     print()
#     ___ idx, s __ en.. s..
#         print('@. @ (length: @, venomous: @)'.f..(
#             ? + 1,
#             ?.n..
#             ?.l..
#             'yes' __ ?.i.. ____ 'no'
#
#
#     snake _ s.. in. in.. 'Which snake do you want to book (number)' - 1
#
#     cages _ s_.g_a_c.. c.. c.. s..
#
#     print("There are @ cages available in that time.".f.. le. ?
#     ___ idx, c __ en.. ?
#         print(" @. @ with @m carpeted: @, has toys: @.".f..(
#             ? + 1,
#             ?.n..
#             ?.s..
#             'yes' __ ?.i.. ____ 'no',
#             'yes' __ ?.h.. ____ 'no'))
#
#     __ no. cages
#         e_m.. "Sorry, no cages are available for that date."
#         r_
#
#     cage _ c.. in. in.. 'Which cage do you want to book (number)' - 1
#     s__.b_c.. s__.a_a.. s.. c.. c.. c..
#
#     success_msg('Successfully booked @ for  at $@/night.'.f.. c__.n.. s__.n.. c__.p..
#
#
# ___ view_bookings(
#     print(' ****************** Your bookings **************** ')
#     __ no. s__.a_a..
#         e_m.. "You must log in first to register a cage"
#         r_
#
#     snakes _ s.id; s ___ s __ s__.g_s_f_u.. s__.a_a...id)
#     bookings _ s__.g_b_f_u.. s__.a_a...email
#
#     print("You have @ bookings.".f.. le. ?
#     ___ b __ ?
#         # noinspection PyUnresolvedReferences
#         print(' * Snake: @ is booked at @ from @ for @ days.'.f..|
#             s__.g.. ?.g_s_i. .n..
#             ?.c__.n..
#             d_t_.d.. ?.c_i_d__.y.. ?.c_i_d__.m.. ?.c_i_d__.d..
#             ?.c_o_d.. - ?.c_i_d.. .d..
#
