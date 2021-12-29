# c_ Solution
#     dx _ 0, 0, -1, 1
#     dy _ 1, -1, 0, 0
#
#     ___ solution board word x y cur
#         __ ? < 0 o.. ? >_ le. b.. o.. ? < 0 o.. ? >_ le. b.. ? o.. b.. ? ? __ ' '
#             r_ F..
#         cur +_ b.. ? ?
#
#         __ le. c.. > le. w..
#             r_ F..
#         __ c.. le. c.. -1 !_ w.. le. c.. - 1
#             r_ F..
#         __ c.. __ w..
#             r_ T..
#
#         temp _ b.. ? ?
#         b.. ? ? _ ' '
#
#         ___ i __ ra.. 4
#             __ .s.. b.. w.. ? + .dx ? ? + .dy ? c..
#                 r_ T..
#
#         b.. ? ? _ t..
#         r_ F..
#
#     ___ exist b.. L.. L.. st. word st.  bo..
#         __ le. w.. __ 0
#             r_ T..
#         n _ le. b..
#         ___ i __ ra.. n
#             m _ le. b.. ?
#             ___ j __ ra.. ?
#                 __ w.. 0 __ b.. ? ? a.. .s.. b.. w.. ? ? ""
#                     r_ T..
#         r_ F..
