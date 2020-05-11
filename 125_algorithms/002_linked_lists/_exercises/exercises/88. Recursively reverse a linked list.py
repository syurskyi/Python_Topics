# c_ Node
#
#     ___ - data_N..
#         ? ?
#         next _ N..
#
#     ___ -s
#         r_ _*|d..
#
# c_ LinkedList
#
#     ___ -
#         head _ N..
#         tail _ N..
#
#     ___ append_val x
#         '''add x to the end of the list'''
#         __ no. isi.. ? N..
#             ? _ N.. ?
#         __ h.. __ N..
#             ? _ ?
#         ____
#             t__.n.. _ ?
#         t.. _ ?
#
#     ___ -s
#         # [5->4->10->1]
#         to_print _ ""
#         curr _ h..
#         w___ c.. __ no. N..
#             t.. +_ st. c__.da.. + "->"
#             c.. _ c__.n..
#         __ to_print
#             r_ "[" + t..|;-2 + "]"
#         r_ "[]"
#
#     ___ add_to_start x
#         '''add x to the left of the list making it the head'''
#         p..
#
#     ___ search_val x
#         '''r_ indices where x was found'''
#         p..
#
#     ___ remove_val_by_index x
#         '''remove and r_ value at index x provided as parameter'''
#         p..
#
#     ___ length
#         '''r_ the length of the list, rep'd by number of nodes'''
#         p..
#
#     ___ reverse_list_recur current, previous):
#         '''reverse the sequence of node pointers in the linked list'''
#         # Given [1->2->3->4->5] reverse pointers [1<-2<-3<-4<-5]
#         # Turning list to [5->4->3->2->1]
#         __ h.. __ N..
#             r_
#         ____ current.next __ N..
#             tail _ h..
#             c__.n.. _ p..
#             h.. _ c..
#         ____
#             n.. _ c__.n..
#             c__.next _ p..
#             r.. n.. c..
#
# my_list _ ?
# ?.append_val(1)
# ?.append_val(2)
# ?.append_val(3)
# ?.append_val(4)
# ?.append_val(5)
# print(?)
# ?.reverse_list_recur(?.head, N..)
# print(?)
