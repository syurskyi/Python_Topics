# ______ ___
# ____ ?.?W.. ______ *
# ____ ?.?C.. ______ __
#
#
# c_ Example ?M..
#
#     ___ -
#         s__ ?  .-
#
#         ?
#
#     ___ initUI
#
#         btn1 _ ?PB.. *Get Amounts of Knobs
#         ?.m.. 30 50
#
#         btn2 _ ?PB.. *Get Name of Node
#         ?.m.. 150, 50
#
#         ?.c__.c.. _1C..
#         ?.c__.c.. _2C..
#
#         sB__
#
#         sG__ 300, 300, 290, 150
#         sWT__ *
#         Event sender
#         s..
#
#     ___ button1Clicked
#
#         num _ nuke.selectedNode .getNumKnobs
#         sB__ .sM.. 'Number of knobs __ Selected node is: ' + st. ?
#
#     ___ button2Clicked
#
#         name _ nuke.selectedNode .knob('name').getValue
#         sB__ .sM.. 'Name of the Selected node is: ' + st. ?
#
#
# __ _____ __ _______
#     ______ ___
#
#     app _ N..
#     ___
#         ______ n..
#     ______ I..
#         app _ ?A.. ___.a..
#     main _ ?
#     ?.s..
#
#     __ app __ no. N..
#         ?.e..