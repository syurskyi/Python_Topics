# """Chain of responsability pattern
# """
# ____ a.. ______ A..
# ______ ra..
#
#
# c_ CannotHandleRequest E..
#     p..
#
#
# c_ Node A..
#
#     ___ -
#         _next_node _ N..
#
#     ___ -s
#         r_ "@".f.. -c . -n
#
#     ??
#     ___ next_node
#         r_ _n..
#
#     ??.?
#     ___ next_node node
#         _next_node _ ?
#
#     ___ handle request $ $$
#         req_name _ ?|*n..
#         req_args _ ?|*a..
#         r_k.. _ ?|*k..
#         method_name _ "@".f.. r_n..
#
#         ___
#             method _ ge.. m_n..
#         ______ A..
#             __ _n.. __ N..
#                 r_ C.. (
#                     'The request "@" could not be handled by any node in the '
#                     "chain".f.. r_n..
#                 |
#
#             _____
#                 print(
#                     'The request "@" cannot be handled by @. Pass request '
#                     "to @".f.. r_n.. st. ? st. n_n..
#                 )
#                 _n____.h.. r.. $ $$
#         _____
#             print(
#                 '@ handles request "@" with arguments @ and keywords @'.f..|
#                     st. ?, r_n.., r_a.., r_k..
#                 )
#             )
#             m.. ?, $ $$
#
#
# c_ WatcherNode N..
#
#     ___ watch  request $ $$
#         # implement actual behavior here
#         string _ "Process request @".f.. ?
#         __ args
#             ? +_ " extra arguments @".f.. a..
#         __ kwargs
#             ? +_ " extra keywords @".f.. k.
#         print ?
#
#
# c_ BuyerNode N..
#
#     ___ buy  request $ $$
#         # implement actual behavior here
#         string _ "Process request @".f.. ?
#         __ args
#             ? +_ " extra arguments @".f.. a..
#         __ kwargs
#             ? +_ " extra keywords @".f.. k.
#         print ?
#
#
# c_ EaterNode N..
#
#     ___ eat  request $ $$
#         # implement actual behavior here
#         string _ "Process request @".f.. ?
#         __ args
#             ? +_ " extra arguments @".f.. a..
#         __ kwargs
#             ? +_ " extra keywords @".f.. k.
#         print ?
#
#
# ___ create_chain $
#     chain _ li..
#     ___ i, node __ en.. a..
#         __ i < le. a.. - 1
#             n__.n_n.. _ a...|? + 1
#         ?.ap.. n..
#     r_ ?
#
#
# ___ request_generator
#     available_requests _ ["buy", "watch", "eat"]
#     available_args _ [(), (123,), (42, 10)]
#     available_kwargs _ [@, {"movie": "Hero"}, {"apple": 3, "color": "red"}]
#     req_num _ ra__.ch..([3, 4, 5])
#     ___ i __ ra.. r_n..
#         r_n.. _ ra__.ch.. a_r..
#         r_a.. _ ra__.ch.. a_a..
#         r_k.. _ ra__.ch.. a_k
#         request _ |"name": r_n.., "args": r_a.., "kwargs": r_k..
#         y... ?
#
#
# # Client
#
#
# ___ main
#     # Client (or a third party) defines a chain of nodes (handlers) at runtime
#     chain _ c_c.. E.., B.. W..
#     root_node _ ? 0
#     ___ i, req __ en.. r_g..
#         print("Request @".f.. ? + 1
#         r_n_.h.. r..
#         print("Request @ with extra arguments/keywords".f.. ? + 1
#         r_n_.h.. r.. 1, 34, key1_44, greet_"hello")
#         print("")
#
#
# __ _______ __ ______
#     ?
