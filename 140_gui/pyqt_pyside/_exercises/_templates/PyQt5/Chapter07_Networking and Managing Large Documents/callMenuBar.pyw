# _____ ___
# ____ ?.?W.. _____ ?M.., ?A..
# ____ ?.?G.. _____ ?P..
#
# ____ demoMenuBar _____ _
#
# c_ AppWindow ?M..
#     ___  -
#         s__. -
#         ui _ ?
#         ?.sU..
#         pos1 _  0 0
#         pos2 _  0 0
#         toDraw_""
#         ?.actionDraw_Circle.t__.c.. dC..
#         ?.actionDraw_Rectangle.t__.c.. dR..
#         ?.actionDraw_Line.t__.c.. dL..
#         ?.actionPage_Setup.t__.c.. pS..
#         ?.actionSet_Password.t__.c.. sP..
#         ?.actionCut.t__.c.. ?
#         ?.actionCopy.t__.c.. ?
#         ?.actionPaste.t__.c.. ?
#         s..
#
#     ___ paintEvent  event
#         qp _ ?P..
#         ?.begin
#         __ toDraw__"rectangle":
#             width _ _2 0-_1 0
#             height _ _2 1 - _1 1
#             ?.dR.. _1 0, _1 1, w.. h..
#         __ toDraw__"line"
#             ?.dL.. _1 0, _1 1, _2 0, _2 1
#         __ tD.. _"circle":
#             width _ _2 0-_1 0
#             height _ _2 1 - _1 1
#             rect _ ?C...?R.. _1 0, _1 1, w.. h..
#             startAngle _ 0
#             arcLength _ 360 *16
#             ?.drA.. r.. sA.. aL..
#         ?.e..
#
#     ___ mousePressEvent  event
#         __ ?.bu.. & ?C...__.LB..
#             _1 0, _1 1 _ ?.pos.x, ?.pos.y
#
#     ___ mouseReleaseEvent , event
#         _2 0, _2 1 _ ?.pos.x, ?.pos.y
#         update
#
#     ___ drawCircle
#         ?.l__.sT.. ""
#         toDraw_"circle"
#
#     ___ drawRectangle
#         ?.l__.sT..("")
#         toDraw_"rectangle"
#
#     ___ drawLine
#         ?.l__.sT..("")
#         toDraw_"line"
#
#     ___ pageSetup
#         ?.l__.sT..("Page Setup menu item is selected")
#
#     ___ setPassword
#         ?.l__.sT..("Set Password menu item is selected")
#
#     ___ cutMethod
#         ?.l__.sT..("Cut menu item is selected")
#
#     ___ copyMethod
#         ?.l__.sT..("Copy menu item is selected")
#
#     ___ pasteMethod
#         ?.l__.sT..("Paste menu item is selected")
#
# app _ ?A..
# w _ ?
# ?.s..
# ___.e.. ?.e


