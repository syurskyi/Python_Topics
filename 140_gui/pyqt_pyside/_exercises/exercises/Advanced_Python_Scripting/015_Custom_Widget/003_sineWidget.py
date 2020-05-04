# ____ __.__ ______ _
# ____ __.__ ______ _
#
# ______ sW.. __ ui
# ____ ma.. ______ sin
#
# c_ sineWidgetClass QW..
#     ___ -
#         s___ ? ?. -
#         sWT.. *Sine
#         r.. 400 200
#
#         wave_height _ 30
#         wave_len _ 20
#         penWidth _ 3
#         grid _ 30
#
#
#     ___ paintEvent event
#         rec _ ?.r..
#         painter _ QP..
#         ?.b.. ?
#
#         # paint
#         ?.fR.. r.. __.bl..
#         ?.sP.. QP.. QB.. __.gr.. 0.5
#         ?.sF.. QF.. 'Arial' 8
#
#         ___ i __ ra.. 0 r__.w.. g..
#             ?.dL.. ? 0 ? r__.h..
#             __ g.. > 20
#                 ?.dT.. ?+3, 12, st. ?
#
#         ___ i __ ra.. 0, r__.h.. g..
#             ?.dL.. 0 ? r__.w.. ?
#
#         ?.sRH.. QP__.A..
#
#         ?.sP.. QP.. QB.. __.w.. pW..
#         prevx _ 0
#         prevy _ 0*w_h.. + r__.h.. /2
#         ___ x __ ra.. 1 r__.w..
#             s _ si. x*0.1)*w_l..*0.1
#             # painter.drawPoint(x, (s * wave_height) + (rec.height()/2))
#             y _  ?*w_h.. + r__.h.. /2
#             ?.dL.. QPF p_x p_y QPF x, y
#             p_x _ x
#             p_y _ y
#             # print x, y
#
#         # end
#         ?.e..
#
#     ___ setHeight v
#         wave_height _ v
#         u..
#
#     ___ setLen v
#         wave_len _ v
#         u..
#
#     ___ setWidth v
#         penWidth _ v
#         u..
#
#     ___ setGrid v
#         grid _ v
#         u..
#
#
# c_ sineWindowClass QM.. __._M..
#     ___ -
#         s__ ? self). -
#         sU.. ?
#         sine _ sWC..
#         s_vL__.aW.. ?
#         h_hS__.sV.. 20
#         l_hS__.sV.. 20
#         g_hS__.sV.. 30
#
#         h_hS__.vC__.c... s___.sH..
#         l_hS__.vC__.c... s___.sL..
#         w_hS__.vC__.c... s___.sW..
#         g_hS__.vC__.c... s___.sG..
#
#
# __ ______ __ ______
#     app _ ?
#     w _ ?
#     ?.s..
#     ?.e..
