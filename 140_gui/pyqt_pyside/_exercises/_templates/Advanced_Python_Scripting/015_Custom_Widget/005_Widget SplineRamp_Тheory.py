# ____ ?.?C.. _____ _
# ____ ?.?G.. _____ _
#
# c_ splineRampWidget ?W..
#     ___  -
#         s__ ? . -
#         r.. 300, 200
#
#         lineWidth _ 3
#         pointSize _ 10
#
#         point1 _ ?P_F 0 0
#         point2 _ ?P_F 300 200
#
#         factor1 _ 0.0
#         factor2 _ 1.0
#
#         dragged _ N..
#
#         region1 _ ?R..
#         region2 _ ?R..
#         regionSize _ 40
#         uR..
#
#     ___ updateRegions
#         region1 _ ?R.. 0 0 rS.. rS..
#         ?.mC.. _1.tP..
#
#         region2 _ ?R.. 0 0 rS.. rS..
#         ?.mC.. _2.tP...
#
#         factor1 _ _1.y / fl.. s__.h..
#         factor2 _ _2.y / fl.. s__.h..
#         print ? ?
#
#     ___ paintEvent  event
#         rec _ ?.r..
#         painter _ ?P..
#         ?.b..
#         ?.sRH.. ?P...A..
#         ?.fR.. ?.r.. __.b..
#         path _ ?PP..
#         ?.mT. _1
#         ?.cT. r__.w../2 _1.y,
#                      r__.w../2, _2.y,
#                      r__.w.. _2.y
#         ?.sP..(?P.. ?B.. __.w.. lW..
#         ?.dP.. p..
#         ?.sB.. ?B.. __.w..
#
#         ?.dE.. _1 pS.. pS..
#         ?.dE.. _2 pS.. pS..
#
#         ?.sP.. ?P.. ?B.. __.w.. 1
#         ?.sB.. __.NB..
#         ?.dR.. _1
#         ?.dR.. _2
#         ?.e..
#
#     ___ mPE..  event
#         # print self.region1.contains(event.pos())
#         __ _1.co.. ?.p..
#             dragged _ _1
#         ____ _2.co.. ?.p..
#             dragged _ _2
#         s__ ? .mPE.. ?
#
#     ___ mouseMoveEvent  event
#         # print self.dragged
#         __ no. dragged __ N..
#             y _ ?.p...y
#             s _ s..
#             dr__.s_Y mi. ma. y 1 s.h..
#             u..
#         s__ ? .mME.. ?
#
#     ___ mouseReleaseEvent event
#         dragged _ N..
#         uR..
#         u..
#         s__ ? .mRE.. ?
#
#     ___ resizeEvent  ?
#
#         _1.s_Y ?.s__.h.. * f_1
#         _2.s_Y ?.s__.h.. * f_2
#         _2.s_X ?.s__.w..
#         uR..
#         u..
#         s__ ? .rE.. ?
#
# __ _____ __ ______
#     app _ ?A..
#     w _ ?
#     ?.s..
#     ?.e..