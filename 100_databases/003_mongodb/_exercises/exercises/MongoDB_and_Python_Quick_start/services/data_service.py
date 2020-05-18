# ____ ty.. ______ L.. O..
#
# ______ d_t_
#
# ______ bson
#
# ____ d__.b..______ B..
# ____ d__.c.. ______ C..
# ____ d__.o.. ______ O..
# ____ d__.s.. ______ S..
#
#
# ___ create_account name st. email st. __ O..
#     owner _ ?
#     ?.? _ ?
#     ?.? _ ?
#
#     ?.s..
#
#     r_ ?
#
#
# ___ find_account_by_email email st. __ O..
#     owner _ ?.o.. e.._e.. .f..
#     r_ ?
#
#
# ___ register_cage active_account O..
#                   name allow_dangerous has_toys
#                   carpeted meters price __ C..
#     cage _ ?
#
#     ?.n.. _ n..
#     ?.square_meters _ meters
#     ?.is_carpeted _ carpeted
#     ?.has_toys _ has_toys
#     ?.allow_dangerous_snakes _ allow_dangerous
#     ?.p.. _ p..
#
#     ?.s..
#
#     account _ f_a_b_e.. a_a_.e..
#     ?.c_i_.ap.. ?.i.
#     ?.s..
#
#     r_ ?
#
#
# ___ find_cages_for_user account O.. __ L.. C..
#     query _ ?.o.. id__in_a__.c_i..
#     cages _ li.. ?
#
#     r_ ?
#
#
# ___ add_available_date cage C..
#                        start_date d_t_.d_t_ days in. __ C..
#     booking _ ?
#     ?.c_i_d.. _ s_d..
#     ?.c_o_d.. _ s_d.. + d_t_.t_d.. d.._d..
#
#     cage _ ?.o.. i_c_.i. .f..
#     ?.b__.ap.. ?
#     ?.s..
#
#     r_ ?
#
#
# ___ add_snake account name length species is_venomous __ S..
#     snake _ ?
#     ?.? _?
#     ?.? _ ?
#     ?.? _ ?
#     ?.? _ ?
#     ?.s..
#
#     owner _ f_a_b_e.. a__.e..
#     ?.s_i__.ap.. ?.i..
#     ?.s..
#
#     r_ ?
#
#
# ___ get_snakes_for_user user_id b__.OI. __ L.. S..
#     owner _ ?.o.. i_u_i. .f..
#     snakes _ ?.o.. id__in_owner.s_i.. .a..
#
#     r_ li.. ?
#
#
# ___ get_available_cages checkin d_t_.d_t_,
#                         checkout d_t_.d_t_ snake S.. __ L.. C..
#     min_size _ sn__.l.. / 4
#
#     query _ ?.o.. \
#         .f..(square_meters__gte_?) \
#         .f..(bookings__check_in_date__lte_?) \
#         .f..(bookings__check_out_date__gte_?)
#
#     __ s__.i..
#         query _ ?.f.. allow_dangerous_snakes_T..
#
#     cages _ ?.o_b.('price', '-square_meters')
#
#     final_cages _   # list
#     ___ c __ c..
#         ___ b __ c.b..
#             __ b.c_i_d.. <_ c.. an b.c_o_d.. >_ c.. an. b.g_s_i __ N..
#                 ?.ap.. c
#
#     r_ ?
#
#
# ___ book_cage account snake cage checkin checkout
#     booking O.. B.. _ N..
#
#     ___ b __ cage.bookings:
#         __ b.check_in_date <_ checkin and b.check_out_date >_ checkout and b.guest_snake_id is N..:
#             booking _ b
#             b..
#
#     ?.g_o_i. _ a__.i.
#     ?.g_s_i _ s__.id
#     ?.c_i_d.. _ c..
#     ?.c_o_d.. _ c..
#     ?.b_d.. _ d_t_.d_t_.n..
#
#     c__.s..
#
#
# ___ get_bookings_for_user email st. __ L.. B..
#     account _ f_a_b_e.. ?
#
#     booked_cages _ ?.o.. \
#         .f.. bookings__guest_owner_id _ a__.i.) \
#         .o..'bookings' 'name'
#
#     ___ map_cage_to_booking cage booking)
#         b__.c.. _ c..
#         r_ ?
#
#     bookings _ |
#         map_cage_to_booking c.. b..
#         ___ cage __ b_c..
#         ___ booking __ c__.b..
#         __ b__.g_o_i. __ a__.i.
#     ]
#
#     r_ ?
