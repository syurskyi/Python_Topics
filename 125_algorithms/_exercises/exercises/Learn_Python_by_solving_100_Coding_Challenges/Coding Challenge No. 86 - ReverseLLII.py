# # Reverse Linked List II
# # Question: Reverse a linked list from position m to n. Do it in-place and in one-pass.
# # For example:
# # Given 1->2->3->4->5->NULL, m = 2 and n = 4,
# # Return 1->4->3->2->5->NULL.
# # Note: Given m, n satisfy the following condition:
# # 1 ≤ m ≤ n ≤ length of list.
# # Solutions:
#
#
# c_ ListNode object
#     ___  -  x
#         val _ x
#         next _ N..
#
#     ___ to_list
#         r_ v.. + n__.t..  __ ? ____ v..
#
#
# c_ Solution object
#     ___ reverseBetween  head m n
#         """
#         :type head: ListNode
#         :type m: int
#         :type n: int
#         :rtype: ListNode
#         """
#         dummy _ ? -1
#         ?.n.. _ h..
#         node _ d..
#         ___ __ __ ra.. m - 1
#             n.. _ ?.n..
#         prev _ ?.n..
#         curr _ p__.n..
#         ___ __ __ ra.. ? - ?
#             n.. _ c__.n..
#             c__.n.. _ p..
#             p.. _ c..
#             c.. _ n..
#         ?.n...n.. _ c..
#         ?.n.. _ p..
#         r_ d__.n..
#
#
# __  -n __ _____
#     n1 _ ? 1
#     n2 _ ? 2
#     n3 _ ? 3
#     n4 _ ? 4
#     n5 _ ? 5
#     n1.n.. _ n2
#     n2.n.. _ n3
#     n3.n.. _ n4
#     n4.n.. _ n5
#     r _ ? .? n1, 2, 4
#     print .to_list