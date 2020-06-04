# ____ ?.?C.. ______ __ ?T..
# ____ ?.?G.. ______ ?P.. ?I..
# ____ ?.?W.. ______ ?W.. ?PTE.., ?PB.., ?VBL.. ?HBL.. ?SI.., ?SP..
#
#
# c_ LogWidget ?W..
#     ___  -   p.._N..
#         s__ ? ? -  p..
#
#         # Base vars
#         logLength _ 0
#         logger _ l__.gL.. -n
#
#         # Palette
#         logPalette _ ?P..
#         ?.sC..(?P...B.. __.bl..
#         ?.sC..(?P...T.. __.y..
#
#         # Text Panel
#         logText _ ?PTE..
#         ?.sP.. lP..
#         ?.sRO.. T..
#
#         # Buttons
#         sendButton _ ?PB.. ?I.. 'img/email.png' 'Send Logs'
#         ?.c__.c__ sL..
#         forceButton _ ?PB.. ?I.. 'img/refresh.png' 'Force Refresh'
#         ?.c__.c__ ?
#         clearButton _ ?PB.. ?I.. 'img/eraser.png' 'Clear Logs'
#         ?.c__.c__ ?
#
#         # Layouts
#         layout _ ?VBL..
#         ?.sCM.. 1, 1, 1, 1
#         ?.aW.. lT..
#
#         buttonLayout _ ?HBL..
#         ?.sCM.. 1, 0, 1, 2
#         ?.aW.. sB..
#         ?.aI..(?SI..(0, 0, ?SP...E.. ?SP...Mi..
#         ?.aW.. fB..
#         ?.aW.. cB..
#
#         l__.aL.. ?
#         sL.. ?
#
#         # Timer
#         logTimer _ ?T..
#         ?.sI.. 5000
#         ?.t__.c__ uL..
#         ?.s..
#
#     ___ sendLogs
#         l__.i.. '[USER] Now sending logs...'
#
#         ___
#             smtp _ smtplib.SMTP 'localhost'
#
#             w__ o.. L_F.. _ __ file
#                 content _ ?.r..
#
#             ?.s.. 'weblord@localhost.com', 'v.ducrocq@gmail.com' ?
#         ______ SMTPE.. __ s
#             l__.e.. '[SYSTEM] Error while sending mail : @'  ?
#             r_
#
#         l__.i.. '[USER] Mail sent!'
#
#     ___ clearLogs
#         l__.i.. '[USER] Clear Logs requested.'
#         o.. L_F.. _ .c..
#         uL..
#
#     ___ updateLog
#         logs _ o.. L_F.. _ .r..
#
#         __ le. ? !_ lL..
#             logL.. _ le. ?
#
#             ?.sPT.. ?
#             ?.mC.. ?TC__.E..
#
#     ___ forceRefresh
#         l__.i.. [USER] Force Log Refresh requested.
#         logLength _ 0
#         uL..
#
#
