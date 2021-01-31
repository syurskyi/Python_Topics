# _____ ?
# _____ n___
#
#
# """
# This module contains functionality to jump directly to the first/last node
# and to connect the viewer with the first/last node
# """
#
#
# ___ get_edge_node which
#     """
#     get most top or bottom node
#     :param which: String first or last node
#     :return: node most top or bottom node
#     """
#
#     edge_node _ N..
#
#     ___ node __ ?.aN..
#
#         __ ?.C..  !_ "Viewer"
#
#             __ e_ __ N..
#                 e_ _ ?
#
#             __ which __ "top":
#                 __ ?.yp__ < e_.yp__
#                     e_ _ ?
#
#             __ which __ "bottom":
#                 __ ?.yp__ > e_.yp__
#                     e_ _ ?
#
#     r_ e_
#
#
# ___ view_edge_node which
#     """
#     connect viewer to first/last node
#     :param which: String first or last node
#     :return: None
#     """
#
#     viewer_port _ 8
#     edge_node _ g.. which
#     sel _ ?.sN..
#
#     __ e_ __ N..
#         r_
#
#     n___.cl..
#     e_.sS.. T..
#     n___.c.. v..
#     e_.sS.. F..
#
#     ___ node __ sel
#         ?.sS.. T..
#
#     ___ ? __ ?.aN.. "Viewer"
#         ?.sS.. F..
#
#
# ___ jump_to_edge_node which
#     """
#     jump to most top or most bottom node
#     :param which: String first or last node
#     :return: None
#     """
#
#     edge_node _ g.. w..
#
#     __ e_ __ N..
#         r_
#
#     ?.z.. 1 fl.. e_.xp__ fl.. e_.yp__
