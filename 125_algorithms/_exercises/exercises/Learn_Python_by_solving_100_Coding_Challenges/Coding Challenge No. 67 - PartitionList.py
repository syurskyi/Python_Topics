# # Partition List
# # Question: Given a linked list and a value x, partition it such that all nodes less than x come before nodes greater than or equal to x.
# # You should preserve the original relative order of the nodes in each of the two partitions.
# # For example,
# # Given 1->4->3->2->5->2 and x = 3,
# # return 1->2->2->4->3->5
# # Solutions:
#
#
# c_ ListNode
#     ___  -  x next_N..
#         val _ ?
#         next _ ?
#
#
# c_ Solution
#     # @param head, a ListNode
#     # @param x, an integer
#     # @return a ListNode
#     ___ partition  head x
#         smaller _ ? -1
#         others _ ? -1
#         smallerLast othersLast _ ? ?
#         w___ h.. !_ N..
#             __ ?.v.. < x
#                 s...n.. _ h..
#                 s.. _ s...n..
#             ____
#                 o__.n.. _ h..
#                 o.. _ ?.n..
#             h.. _ ?.n..
#         s...n.. _ o__.n..
#         o__.n.. _ N..
#         r_ s__.n..
#
#     ___ printll node
#         w___ ?
#             print ?.v..
#             n.. _ ?.n..
#
#
# __  -n __ ______
#     node6 _ ? 2
#     node5 _ ? 5 ?
#     node4 _ ? 2 ?
#     node3 _ ? 3 ?
#     node2 _ ? 4 ?
#     ll1 _ ? 1, node2
#     ? .p.. ? .? ? 3