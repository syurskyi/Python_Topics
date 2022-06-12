# ____ c.. _______ n..
# ____ d__ _______ d__
# ____ o.. _______ i__
# ____ t___ _______ L..
#
# Sign n..('Sign', 'name compatibility famous_people sun_dates')
#
#
# ___ get_signs data l.. __ L.. ?
#     ret    # list
#     ___ sign __ ?
#         name ? name
#         compatibility ? compatibility
#         famous_people ? famous_people
#         sun_dates ? sun_dates
#         ? ? ? ? ? ?
#         ?.a..
#             ?
#
#     r.. ?
#
#
# ___ get_sign_with_most_famous_people signs l..
#     """Get the sign with the most famous people associated"""
#     f..
#         s.n.. l.. ?.f.. ___ ? __ ?
#
#     r.. m.. ? k.._i.. 1
#
#
# ___ signs_are_mutually_compatible signs l.., sign1 s.. sign2 s.. __ b..
#     """Given 2 signs return if they are compatible (compatibility field)"""
#     ret F..
#     ___ sign __ ?
#         __ ?.n.. __ ?1
#             r.. ?2 __ ?.c..
#         ____ ?.n.. __ sign2:
#             r.. ?1 __ ?.c..
#     r.. ?
#
#
# ___ get_sign_by_date signs l.. date d__ __ s..
#     """Given a date return the right sign (sun_dates field)"""
#     year ?.y..
#     ___ sign __ ?
#         start, end ?.s..
#         start_dt d__.s.. ? _B _d .r.. y.._?
#         end_dt d__.s.. > _B _d .r.. y.._?
#         __ ? < ?
#             __ date <_ e..
#                 s.. d__.s.. ? _B _d .r.. y.._?-1
#             ____
#                 e.. d__.s.. ? _B _d .r.. y.._?+1
#         __ s.. <_ ? <_ e..
#             r.. ?.n..