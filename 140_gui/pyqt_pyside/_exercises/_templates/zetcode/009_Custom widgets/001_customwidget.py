# #!/usr/bin/python3
# # -*- coding: utf-8 -*-
#
#
# ____ ?.?W.. ______  W..  ?S..  ?A..
#                              ?HB..  ?VB..
# ____ ?.?C.. ______ ?O..  __  pyqtS..
# ____ ?.?G__ ______ ?P..  QFont  ?C..  ?P..
# ______ ___
#
#
# c_ Communicate ?O..
#     updateBW _ pyqtS.. in..
#
#
# c_ BurningWidget W..
#
#     ___ -
#         s__ .-
#
#         ?
#
#     ___ initUI
#
#         sMS.. 1  30
#         value _ 75
#         num _ [75  150  225  300  375  450  525  600  675]
#
#     ___ sV.. value
#
#         ? ?
#
#     ___ paintEvent e
#
#         qp _ ?P..
#         ?.b..
#         dW.. ?
#         ?.e..
#
#     ___ drawWidget qp
#
#         MAX_CAPACITY _ 700
#         OVER_CAPACITY _ 750
#
#         font _ ?F.. 'Serif' 7 ?F__.L..
#         ?.sF.. ?
#
#         size _ s..
#         w _ ?.w..
#         h _ ?.h..
#
#         step _ in. ro.. w / 10
#
#         till _ in. w / O.. ) * va..
#         full _ in. w / O.. ) * M..
#
#         __ value >_ M..
#
#             ?.sP.. ?C.. 255  255  255
#             ?.sB.. ?C.. 255  255  184
#             ?.dR.. 0  0  full  h
#             ?.sP.. ?C.. 255  175  175
#             ?.sB.. ?C.. 255  175  175
#             ?.dR.. full  0  till - full  h
#
#         ____
#
#             ?.sP.. ?C.. 255  255  255
#             ?.sB.. ?C.. 255  255  184
#             ?.dR.. 0  0  till  h
#
#         pen _ ?P.. ?C.. 20  20  20)  1
#                    __.SL..
#
#         ?.sP.. ?
#         ?.sB.. __.NB..
#         ?.dR.. 0  0  w - 1  h - 1
#
#         j _ 0
#
#         ___ i __ ra.. s.. 10 * s.. s..
#             ?.dL.. i  0  i  5
#             metrics _ ?.fM..
#             fw _ ?.wi.. st. num j
#             ?.dT.. i - fw / 2  h / 2  st. num j
#             j _ j + 1
#
#
# c_ Example W..
#
#     ___ -
#         s__ .-
#
#         ?
#
#     ___ initUI
#         OVER_CAPACITY _ 750
#
#         sld _ ?S.. __.H..
#         ?.sFP.. __.NoF..
#         ?.sR.. 1  O..
#         ?.sV.. 75
#         ?.sG__ 30  40  150  30
#
#         c _ C..
#         wid _ BW..
#         c.uBW|in. .c.. ?.sV..
#
#         ?.vC__|in. .c.. cV..
#         hbox _ ?HB..
#         ?.aW.. w..
#         vbox _ ?VB..
#         ?.aS.. 1
#         ?.aL.. ?
#         sL.. ?
#
#         sG__ 300  300  390  210
#         sWT__ 'Burning widget')
#         s..
#
#     ___ changeValue  value
#         c.uBW.e.. ?
#         w__.re..
#
#
# __ _____ __ _______
#     app _ ?A..
#     ex _ ?
#     ___.e.. ?.e..