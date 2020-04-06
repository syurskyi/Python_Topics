# ____ d.. _______ d_t.. t_d..
#
# c_ Node
#     ___ - key
#         sched_time, duration, name_of_job _ ?.sp.. ","
#         raw_sched_time _ d_t_.s_t.. s_t.. '%H:%M'
#         key _ ?.ti..
#         end_time _ r.. + t__d.. m_i.. d___ .ti..
#         data _ k..
#         scheduled_end _ e..
#         duration _ ?
#         name_of_job _ n__.rs
#         left_child _ N..
#         right_child _ N..
#
#     ___ -
#         r_ _*Time: |? Duration: |?, End: |?, Jobname: |?
#
# c_ BSTDemo
#     ___ -
#         root _ N..
#
#     ___ insert key
#         __ no. isi.. ? ?
#             ? _ ? ?
#         __ r.. __ N..
#             r.. _ ?
#             h.. k.. T..
#         ____
#             _? r.. k..
#
#     ___ _insert curr key
#         __ k__.d.. > ?.d.. an. k__.d.. >_ ?.s..
#             __ ?.r.. __ N..
#                 ?.r.. _ k__
#                 h.. k__ T..
#             ____
#                 _? ?.r.. k__
#         ____ k__.d.. < ?.d.. an. k__.s.. <_ ?.d..
#             __ ?.l.. __ N..
#                 ?.l.. _ k__
#                 h.. k__ T..
#             ____
#                 _? ?.l.. k__
#         ____
#             h.. k__ F..
#
#     ___ helpful_print key succeeded
#         __ s..
#             print(_*Added:\t\t |?.n..
#             print(_*Begin:\t\t |?.d..
#             print(_*End:\t\t |?.s..
#             print("-"*60)
#         ____
#             print(_*Rejected:\t |?.n..
#             print(_*Begin:\t\t |?.d..
#             print(_*End:\t\t |?.s..
#             print("Reason:\t Time slot overlap, please verify")
#             print("-"*60)
#
#     ___ in_order
#         print("Full job schedule for today")
#         print("-"*60)
#         _? r..
#         print("-"*60)
#
#     ___ _in_order curr
#         __ ?
#             _? ?.l..
#             print(?)
#             _? ?.r..
#
#     ___ length
#         r_ _? r..
#
#     ___ _length curr
#         __ ? __ N..
#             r_ 0
#         r_ 1 + _? ?.l.. + _? ?.r..
#
#     ___ find_val key
#         r_ _? r.. ?
#
#     ___ _find_val curr key
#         __ ?
#             __ ? __ ?.d..
#                 r_ ?
#             ____ ? < ?.d..
#                 r_ _? ?.l.. ?
#             ____
#                 r_ _? ?.r.. ?
#         r_
#
#     ___ min_right_subtree curr
#         __ ?.l.. __ N..
#             r_ ?
#         ____
#             r_ ? ?.l..
#
#     ___ delete_val key
#         _? r.. N.. N.. ?
#
#     ___ _delete_val curr prev is_left key
#         __ ?
#             __ k__ __ ?.d..
#                 __ ?.l.. an. ?.r..
#                     min_child _ m.. ?.r..
#                     ?.d.. _ ?.d..
#                     _? ?.r.. ? F.. ?.d..
#                 ____ ?.l.. __ N.. an. ?.r.. __ N..
#                     __ p..
#                         __ i..
#                             p__.l.. _ N..
#                         ____
#                             p__.r.. _ N..
#                     ____
#                         r.. _ N..
#                 ____ ?.l.. __ N..
#                     __ p..
#                         __ i..
#                             p__.l.. _ ?.r..
#                         ____
#                             p__.r.. _ ?.r..
#                     ____
#                         r.. _ ?.r..
#                 ____
#                     __ p..
#                         __ i..
#                             p__.l.. _ ?.l..
#                         ____
#                             p__.r.. _ ?.l..
#                     ____
#                         r.. _ ?.l..
#             ____ k__ < ?.d..
#                 _d.. ?.l.. ? T.. k__
#             ____ k__ > ?.d..
#                 _de(?.r.. ? F.. k__
#         ____
#             print(_*|k__ no. found in Tree")
