# ____ __.__ ______ _
# ____ __.__ ______ _
# 
# c_ splineRampWidget QW..
#     ___ -
#         s__ ? ?. -
#         r.. 300, 200
# 
#         lineWidth _ 3
#         pointSize _ 10
# 
#         point1 _ QPF 0, 0
#         point2 _ QPF(300, 200
# 
#         factor1 _ 0.0
#         factor2 _ 1.0
# 
#         dragged _ N..
# 
#         region1 _ QR..
#         region2 _ QR..
#         regionSize _ 40
#         uR..
# 
#     ___ updateRegions
#         region1 _ QR.. 0 0 regionSize regionSize
#         ?.mC.. p_1.tP..
# 
#         region2 _ QR.. 0 0 regionSize regionSize
#         ?.mC.. p_2.tP..
# 
#         factor1 _ p_1.y / fl.. s...h..
#         factor2 _ p_2.y / fl.. s...h..
#         print ?  ?
# 
#     ___ paintEvent event
#         rec _ ?.r..
#         painter _ QP..
#         ?.b.. ?
#         ?.sRH..QP___.An..
#         ?.fR.. ?.r.. __.bl..
#         path _ QPP..
#         ?.mT. p_1
#         ?.cT. r__.w.. /2, p_1.y
#                      r__.w../2 p_2.y
#                      r__.w.. p_2.y
#         ?.sP.. QP.. QB.. __.wh.. lW..
#         ?.dP.. ?
#         ?.sB.. QB.. __.wh..
# 
#         ?.dE.. p_1 pS.. pS..
#         ?.dE.. p_2 pS.. pS..
# 
#         ?.sP.. QP.. QB.. __.wh.. 1
#         ?.sB.. (__.NB..
#         ?.dR.. r_1
#         ?.dR.. r_2
#         ?.e..
# 
#     ___ mousePressEvent event
#         # print region1.contains(event.pos())
#         __ r_1.co.. ?.p..
#             dragged _ p_1
#         ____ r_2.co.. ?.p..
#             dragged _ p_2
#         s___ ? ?.mPE.. ?
# 
#     ___ mouseMoveEvent event
#         # print dragged
#         __ not dragged is None:
#             y _ ?.p__.y
#             s _ si..
#             dr__.s_Y mi. ma. y 1 ?.h..
#             u..
#         s___ ? ?.mME.. ?
# 
#     ___ mouseReleaseEvent event
#         dragged _ N..
#         uR..
#         u..
#         s___ ? ?.mRE.. ?
# 
#     ___ resizeEvent event
# 
#         p_1.s_Y ?.s__.h.. * f_1
#         p_2.s_Y ?.s__.h.. * f_2
#         p_2.s_X ?.s__.w..
#         uR..
#         u..
#         s___ ? ?.rE.. ?
# 
# __ ______ __ ______
#     app _ ?
#     w _ ?
#     ?.s..
#     ?.e..
