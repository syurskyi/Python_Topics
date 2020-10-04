# # Add Two Numbers
# # Question: You are given two linked lists representing two non-negative numbers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.
# # Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
# # Output: 7 -> 0 -> 8
# # Solutions:
#
# c_ ListNode
#     ___  -  x
#         val _ x
#         next _ N..
#
# c_ Solution
#     ___ addTwoNumbers l1 l2
#         dummy _ ? 0
#         current, carry _ ? 0
#         w___ ? o. ?
#             v.. _ c..
#             __ ?
#                 v.. +_ ?.v..
#                 l1 _ ?.n..
#             __ ?
#                 ? +_ ?.v..
#                 l2 _ ?.n..
#                 c.. v.. _ ? / 10 ? % 10
#                 c__.n.. _ ? ?
#                 c.. _ c__.n..
#             __ c.. __ 1
#                 c__.n.. _ ? 1
#             r_ ?.n..
#
# __  -n __ ______
#     a, a.n.., a.n...n.. _ ? 2, ? 4, ? 3
#     b, b.n.., b.n...n.. _ ? 5, ? 6, ? 4
#     result _ ?.? ?
#     print  "@ -> @ -> @".f.. in. r__.v.. in. r__.n...v.. in. r__.n...n...v..