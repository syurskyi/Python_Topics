# #
# c_ Truth
#    ___ -b ____ r_ T...
#
# X = ?
# i_ ? print('yes!')
#
# c_ Truth:
#    ___ -b ____ r_ F..
#
# X = ?
# print b.. ?
#
# c_ Truth
#    ___ -l ____ r_ 0
# #
# X = ?
# i_ no. X print('no!')
#
# c_ Truth
#    ___ -b ____ r_ T...            # 3.0 tries __bool__ first
#    ___ -l ____ r_ 0                # 2.6 tries __len__ first
#
# X = ?
# i_ ? print('yes!')
#
# c_ Truth
#     p...
#
# X = ?
# bo.. ?
#
# c_ C
#     ___ -b ____
#         print('in bool')
#         r_ F..
#
# X = ?
# bo. ?
#
# # in bool
#
# i_ X: print(99)
#
# # in bool
#
# c_ C:
#     ___ -b ____
#         print('in bool')
#         r_ F..
#
# X = ?
# bo.. ?
#
# if X: print(99)
#
# c_ C:
#     ___ no... ____
#         print('in nonzero')
#         r_ F..
#
# X = C()
# bool(X)
# # in nonzero
#
# if X: print(99)
#
# # in nonzero

