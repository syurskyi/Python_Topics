# # Open-Closed Principle (OCP)
#
# # Classes should be open for extension but closed for modification.
# ____ a.. _______ A.. a..
# ____ ty.. _______ L..
#
#
# c_ Journal:
#     ___ -
#         ?entries L..|s.. _    # list
#         ?count i.. _ 1
#
#     ___ add_entry text ? __ N..
#         ?e___.ap..  _*|c__. |t.. ")
#         c.. +_ 1
#
#     ___ __str__
#         r_ "\n".j.. ?e___
#
#     ___ save  storage_manager "S..M..", name ? __ N..
#         s_m_.s.. ____ n..
#
#
# c_ StorageManager A..
#     ??
#     ___ save  journal J.. name ?
#         p..
#
#
# c_ LocalStorageManager S..
#     ___ save journal J.. name ?
#         w___ o.. ? _ __ f
#             print(_*Saving journal |n..| into local storage.")
#             ?.w.. st. j..
#
#
# c_ ExternalStorageManager S..
#     ___ save  journal J.. name ?
#         print(_*Saving journal |n..| into external storage.")
#
#
# __ _______ __ _____
#     journal = J..
#     ?.a___("Today, I'm learning about the Open-Closed Principle.")
#     ?.a___("Yesterday, I've learned about the Single-Responsibility Principle.")
#     print ?
#
#     external_storage_manager = L..
#     j___.s.. ? "my_journal"
#
#     external_storage_manager = E..
#     j__.s.. ?, "my_journal"
