# ______ d_t_
# ____ co.. ______ F..
# ____ dateutil ______ pa..
#
# ____ i__.s.. ______ s..
# ______ i__.s..__ state
# ______ s__.d_s.. __ svc
#
#
# ___ r..
#     print(' ****************** Welcome host **************** ')
#     print()
#
#     s_c
#
#     w__ T..
#         action _ g_a..
#
#         w__ s.. ? __ s
#             ?.c.. 'c' c_a..
#             ?.c.. 'a' c_a..
#             ?.c.. 'l' l_i_a..
#             ?.c.. 'y' l_c..
#             ?.c.. 'r' r..
#             ?.c.. 'u' u..
#             ?.c.. 'v' v..
#             ?.c.. 'm' l___ 'change_mode'
#             ?.c.. 'x', 'bye', 'exit', 'exit()' e..
#             ?.c.. '?', s_c..
#             ?.c.. '', l___ N..
#             ?.d.. u..
#
#         __ action
#             print()
#
#         __ ?.r.. __ 'change_mode':
#             r_
#
#
# ___ show_commands
#     print('What action would you like to take:')
#     print('[C]reate an [a]ccount')
#     print('[L]ogin to your account')
#     print('List [y]our cages')
#     print('[R]egister a cage')
#     print('[U]pdate cage availability')
#     print('[V]iew your bookings')
#     print('Change [M]ode (guest or host)')
#     print('e[X]it app')
#     print('[?] Help (this info)')
#     print()
#
#
# ___ create_account
#     print(' ****************** REGISTER **************** ')
#
#     name _ in.. 'What is your name? '
#     email _ in.. 'What is your email? ' .s.. .l..
#
#     old_account _ s__.f_a_b_m.. ?
#     __ ?
#         e_m.. _*ERROR: Account with email |e.. already exists.")
#         r_
#
#     s__.active_account _ s__.c_a.. n.. e..
#     s_m.. _*Created new account with id {s__.a_a__.i.
#
#
# ___ log_into_account
#     print(' ****************** LOGIN **************** ')
#
#     email _ in..('What is your email? ').s.. .l..
#     account _ s__.f_a_b_m.. ?
#
#     __ no. ?
#         e_m.. _*Could not find account with email |e..
#         r_
#
#     s__.a_a.. _ ?
#     s_m..('Logged in successfully.')
#
#
# ___ register_cage
#     print(' ****************** REGISTER CAGE **************** ')
#
#     __ no. s__.active_account:
#         e_m..('You must login first to register a cage.')
#         r_
#
#     meters _ in..('How many square meters is the cage? ')
#     __ no. ?
#         e_m..('Cancelled')
#         r_
#
#     meters _ fl.. ?
#     carpeted _ in.. "Is it carpeted [y, n]? " .l...s_w.. 'y'
#     has_toys _ in.. "Have snake toys [y, n]? " .l...s_w.. 'y'
#     allow_dangerous _ in..("Can you host venomous snakes [y, n]? " .l...s_w.. 'y'
#     name _ in.. "Give your cage a name: "
#     price _ fl.. in.. "How much are you charging?  "
#
#     cage _ s__.r_c..|
#         s__.a_a.. n..
#         a.. h.. c.. m.. p..
#
#
#     s__.r_a..
#     s_m.. _*Register new cage with id |c__.i. .
#
#
# ___ list_cages suppress_header_F..
#     __ no. ?
#         print(' ******************     Your cages     **************** ')
#
#     __ no. s__.a_a..
#         e_m..('You must login first to register a cage.')
#         r_
#
#     cages _ s__.f_c_f_u.. s__.a_a..
#     print _*You have |l.. c..| cages.")
#     ___ idx, c __ en.. ?
#         print _* |i.. + 1 . |?.n..| is |?.s_m..| meters.')
#         ___ b __ ?.b..
#             print('      * Booking: @, @ days, booked? @'.f..(
#                 ?.c..
#                 (?.c.. - ?.c.. .d..
#                 'YES' __ ?.b.. __ no. N.. ____ 'no'
#
#
#
# ___ update_availability
#     print(' ****************** Add available date **************** ')
#
#     __ no. s__.a_a..
#         e_m..("You must log in first to register a cage")
#         r_
#
#     list_cages suppress_header_T..
#
#     cage_number _ in..("Enter cage number: ")
#     __ no. c_n_.s..
#         e_m..('Cancelled')
#         print()
#         r_
#
#     cage_number _ in. c_n..
#
#     cages _ s__.f_c_f_u.. s__.a_a..
#     selected_cage _ ? c_n.. - 1
#
#     s_m..("Selected cage @".f.. s_c__.n..
#
#     start_date _ p__.p..
#         in.. "Enter available date [yyyy-mm-dd]: "
#
#     days _ in. in.. "How many days is this block of time? "
#
#     s__.a_a_d..
#         s_c..
#         s_d..
#         d..
#
#
#     s_m.. _*Date added to cage |s_c__.n.. .
#
#
# ___ view_bookings
#     print(' ****************** Your bookings **************** ')
#
#     __ no. s__.a_a..
#         e_m..("You must log in first to register a cage")
#         r_
#
#     cages _ s__.f_c_f_u.. s__.a_a..
#
#     bookings _ |
#         (c, b)
#         ___ c __ ?
#         ___ b __ ?.b..
#         __ ?.b_d.. __ no. N..
#
#
#     print("You have @ bookings.".f.. le. ?
#     ___ c, b __ ?
#         print(' * Cage: @, booked date: @, from @ for @ days.'.f..
#             ?.n..
#             d_t_.d.. ?.b_d_.y.. ?.b_d_.m.. ?.b_d_.d..
#             d_t_.d.. ?.c_i_d_.y.. ?.c_i_d_.m.. ?.c_i_d_.d..
#             ?.d_i_d..
#
#
#
# ___ exit_app
#     print()
#     print('bye')
#     r_ Ke..
#
#
# ___ get_action
#     text _ '> '
#     __ s__.a_a..
#         text _ _*|s__.a_a...n.. > '
#
#     action _ in.. ?.Y.. + ? + ?.W..
#     r_ ?.s.. .l..
#
#
# ___ unknown_command
#     print("Sorry we didn't understand that command.")
#
#
# ___ success_msg text
#     print(?.L.. + ? + ?.W..
#
#
# ___ e_m.. text
#     print(?.L.. + ? + ?.W..
