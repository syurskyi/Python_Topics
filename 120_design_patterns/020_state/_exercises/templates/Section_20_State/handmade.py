# ____ en.. ______ E.. a..
#
#
# c_ State E..
#     OFF_HOOK _ ?
#     CONNECTING _ ?
#     CONNECTED _ ?
#     ON_HOLD _ ?
#     ON_HOOK _ ?
#
#
# c_ Trigger E..
#     CALL_DIALED _ ?
#     HUNG_UP _ ?
#     CALL_CONNECTED _ ?
#     PLACED_ON_HOLD _ ?
#     TAKEN_OFF_HOLD _ ?
#     LEFT_MESSAGE _ ?
#
#
# __ ________ __ _______
#     rules _ |
#         S___.O...: |
#             |T_____.C_D.. S___.C..
#         ],
#         S___.C.. |
#             |T_____.H.. S___.O..
#             |T_____.C_C.. S___.C...
#         |,
#         S___.C..: |
#             |T_____.L.. S___.O_HOL..
#             |T_____.H_U. S___.O_HOO
#             |T_____.P_O_H.. S___.O_HOL.
#         |,
#         S___.O_H: |
#             |T_____.T_O_H.. S___.C..
#             |T_____.H_U. S___.O_H..
#         |
#     |
#
#     state _ S___.O...
#     exit_state _ S___.O._HOO.
#
#     w____ ? !_ ?
#         print _*The phone is currently |?')
#
#         ___ i __ ra.. le. ru.. |?
#             t _ r.. ? ?|0
#             print _*|?: |?')
#
#         idx _ in. in.. 'Select a trigger:'
#         s _ r..|?|?|1
#         state _ s
#
#     print('We are done using the phone.')