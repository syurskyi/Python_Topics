# ____ __.__ ______ _
# ____ __.__ ______ _
#
#
# c_ editorItemClass QG..
#     ___ - height num
#         s___ ? ? . -
#         x _ 0
#         y _ 0
#         w _ 150
#         h _ height
#         num _ num
#         hover _ N..
#         setAcceptHoverEvents T..
#         resizePadding _ 10
#         resizeL _ F..
#         resizeR _ F..
#         startPos _ N..
#         sF. QGI_.II_M.. _ QGI_.IIS..
#
#     ___ boundingRect
#         r_ QR.. x y w h
#
#     ___ paint painter opt w
#         rec _ bR..
#         __ F..
#             painter _ QP..
#         ?.fR.. rec __.bl..
#         ?.fR.. r__.ad.. 1,1,-1,-1 __.wh..
#         __ no. h..
#             color _ __.dG..
#         ____
#             color _ __.gr..
#         __ iS..
#             color _ __.y..
#         ?.fR.. r__.ad.. 3,3,-3,-3 c..
#
#         ?.sF.. QF.. 'Arial' 10
#         ?.sP.. QP.. __.bl..
#         ?.dT.. r__ __.AC.. 'Node @'  n..
#
#         ?.sP.. __.NP..
#
#         ?.fR.. QR.. x+4,4,rP.. h-8), __.r..
#         ?.fR.. QR.. x+w-4-rP... 4 rP.. h-8), __.r..
#
#
#     ___ adjustpos
#         y _ p__.y
#         delta _ y % h
#         __ ? > h / 2
#             delta _ h - ?
#             sP.. p.. + QP.. 0 ?
#         ____
#             sP.. p.. - QP.. 0 ?
#
#     ___ checkCollision
#         coll _sc__ .cI..
#         __ ?
#             sP.. p.. -QP.. 0 h
#             cC..
#
#     ___ hoverMoveEvent event
#         p _ ?.p__.x
#         __ x < p < x + rP..
#             sC.. __.SHC..
#             resizeL _ T..
#         ____ x+w - rP... < p < w+x:
#             sC.. __.SHC..
#             resizeR _ T..
#         ____
#             sC.. __.SAC..
#             resizeR _ resizeL _ F..
#         s___ ? ? .hME.. ?
#
#     ___ hoverEnterEvent  event
#         hover _ T..
#         s___ ? ? .hEE.. ?
#
#     ___ hoverLeaveEvent  event
#         hover _ F..
#         s___ ? ? .hLE.. ?
#
#     ___ mousePressEvent  event
#         startPos _ ?.p..
#         s___ ? ? .mPE.. ?
#
#     ___ mouseMoveEvent  event
#         __ resizeL o. resizeR
#             delta _ sP.. - ?.p__.x
#             startPos _ ?.p..
#             __ resizeL
#                 tmp1 _ x
#                 tmp2 _ w
#                 x _ x - d..
#                 w _ w + d..
#                 __ sc__.cI.. ?
#                     x _ _1
#                     w _ _2
#             ____
#                 tmp _ w
#                 w -_ d___
#                 __ sc__.cI.. ?
#                     w _ tmp
#             sc___.up..
#         ____
#             s___ ? ? .mME.. ?
