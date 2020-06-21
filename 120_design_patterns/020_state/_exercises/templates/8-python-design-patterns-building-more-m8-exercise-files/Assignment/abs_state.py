# ______ a..
#
# STATETRANSITIONERROR _ 'Cannot add an item while in the %s state'
#
# c_ AbsState m..
#     ___ - context
#         _cart _ ?
#
#     ___ add_item
#         _t..
#
#     ___ remove_item
#         _t..
#
#     ___ checkout
#         _t..
#
#     ___ pay
#         _t..
#
#     ___ empty_cart
#         _t..
#
#     ___ suspend
#         _c__.s_s.. _ _c__.st..
#         _c__.st.. _ _c__.su..
#
#     ___ resume
#         _t..
#
#     ___ _transition_error
#         r_ N.. |
#             S..  _c__.s__. -c. -n
