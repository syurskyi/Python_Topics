# _____ ___
# ____ ?.?W.. _____ ?M.., ?A..
# ____ ?.?G.. _____ ?P..
#
# ____ demoToolBars _____ _
#
# c_ AppWindow ?M..
#     ___  -
#         s__. -
#         ui _ Ui_MainWindow
#         ?.setupUi
#         pos1 _  0 0
#         pos2 _  0 0
#         toDraw_""
#         ?.aC__.t__.c.. dC..
#         ?.aR__.t__.c.. dR..
#         ?.aL__.t__.c.. dL..
#         s..
#
#     ___ paintEvent  event
#         qp _ ?P..
#         ?.b..
#         __ toDraw__"rectangle"
#             width _ _2 0 -_1 0
#             height _ _2 1  - _1 1
#             ?.dR.. _1 0   _1 1   w..  h..
#         __ tD..__"line"
#             ?.dL.. _1 0   _1 1   _2 0   _2 1 )
#         __ tD..__"circle":
#             width _ _2 0 -_1 0
#             height _ _2 1  - _1 1
#             rect _ ?C...?R..(_1 0   _1 1   w..  h..
#             startAngle _ 0
#             arcLength _ 360 *16
#             ?.dA.. r..  sA..  aL..
#         ?.e..
#
#     ___ mousePressEvent   event
#         __ ?.buttons & ?C...__.LB..:
#             _1 0   _1 1  _ ?.p...x  ?.p...y
#
#     ___ mouseReleaseEvent   event
#         _2 0   _2 1  _ ?.p...x  ?.p...y
#         u..
#
#     ___ drawCircle
#         toDraw_"circle"
#
#     ___ drawRectangle
#         toDraw_"rectangle"
#
#     ___ dL..
#         toDraw_"line"
#
# app _ ?A..
# w _ AppWindow
# ?.s..
# ___.e.. ?.e
#
#
#
#
