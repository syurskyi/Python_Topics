# c_ Person
#     ___ - name
#         ?  ?
#         chat_log _   # list
#         room _ N..
#
#     ___ receive sender message
#         s _ _*|?: |?'
#         print(_*[|n..\'s chat session] |?')
#         c_l__.ap.. ?
#
#     ___ say message
#         r___.b.. n.. m..
#
#     ___ private_message who message
#         r___.m.. n.. w.. m..
#
#
# c_ ChatRoom
#     ___ -
#         people _    # list
#
#     ___ broadcast source message
#         ___ p __ people
#             __ ?.n.. !_ s..
#                 p.re.. s.. m..
#
#
#     ___ join person
#         join_msg _ _*|?.n..| joins the chat'
#         b..('room' ?
#         p___.r___ _ ?
#         pe___.ap.. ?
#
#
#     ___ message source destination message
#         ___ p __ people
#             __ ?.name __ d...
#                 ?.re.. s.. m..
#
#
# __ _______ __ ______
#     room _ C..
#
#     john _ P.. 'John'
#     jane _ P.. 'Jane'
#
#     r__.jo.. jo..
#     r__.jo.. ja..
#
#     john.s.. 'hi room')
#     jane.s.. 'oh, hey john')
#
#     simon _ P.. 'Simon'
#     r__.j.. ?
#     ?.say('hi everyone!')
#
#     jane.p_m..('Simon', 'glad you could join us!')