# # Linked List Nth to Last Node - SOLUTION
# # Problem Statement
# #
# # Write a function that takes a head node and an integer value n and then returns the nth to last node in the linked list. For example, given:
# #
# c_ Node
#
#     ___ - value
#         ?  ?
#         nextnode  _ N..
#
# a = Node(1)
# b = Node(2)
# c = Node(3)
# d = Node(4)
# e = Node(5)
#
# a.nextnode = b
# b.nextnode = c
# c.nextnode = d
# d.nextnode = e
#
# # # This would return the node d with a value of 4, because its the 2nd to last node.
# target_node = nth_to_last_node(2, a)
# #
# target_node.value
# # 4
# #
# # Solution
# # One approach to this problem is this:
# # Imagine you have a bunch of nodes and a "block" which is n-nodes wide. We could walk this "block" all the way down
# # the list, and once the front of the block reached the end, then the other end of the block would be a the Nth node!
# # So to implement this "block" we would just have two pointers a left and right pair of pointers. Let's mark out
# # the steps we will need to take:
# #
# #     Walk one pointer n nodes from the head, this will be the right_point
# #     Put the other pointer at the head, this will be the left_point
# #     Walk/traverse the block (both pointers) towards the tail, one node at a time, keeping a distance n between them.
# #     Once the right_point has hit the tail, we know that the left point is at the target.
# #
# # Let's see the code for this!
# #
# ___ nth_to_last_node n head
#
#     left_pointer  _ head
#     right_pointer _ head
#
#     # Set right pointer at n nodes away from head
#     __ i __ ra.. ?-1
#
#         # Check for edge case of not having enough nodes!
#         __ no. r__.n..
#             r_ L.. 'Error: n is larger than the linked list.'
#
#         # Otherwise, we can set the block
#         r__ _ ?.n..
#
#     # Move the block down the linked list
#     w__ r__.n...
#         l__  _ ?.n..
#         r__ = ?.n..
#
#     # Now return left pointer, its at the nth to last element!
#     r_ ?
#
# # Test Your Solution
# #
# # """
# # RUN THIS CELL TO TEST YOUR SOLUTION AGAINST A TEST CASE
# #
# # PLEASE NOTE THIS IS JUST ONE CASE
# # """
# #
# from nose.tools import assert_equal
#
# a = Node(1)
# b = Node(2)
# c = Node(3)
# d = Node(4)
# e = Node(5)
#
# a.nextnode = b
# b.nextnode = c
# c.nextnode = d
# d.nextnode = e
#
# ####
#
# c_ TestNLast o..
#
#     ___ test,sol
#
#         a_e_ ?(2,a),d)
#         print 'ALL TEST CASES PASSED'
#
# # Run tests
# t = TestNLast()
# t.test(nth_to_last_node)
# #
# # ALL TEST CASES PASSED
# #
# # Good Job!