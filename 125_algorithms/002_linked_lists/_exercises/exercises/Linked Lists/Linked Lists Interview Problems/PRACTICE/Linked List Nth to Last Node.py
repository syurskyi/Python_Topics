# # Linked List Nth to Last Node
# # Problem Statement
# #
# # Write a function that takes a head node and an integer value n and then returns the nth to last node in the linked list. For example, given:
#
# c_ Node
#
#     ___ - value
#         ? ?
#         nextnode  _ N..
#
# # Example Input and Output:
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
#
# target_node.value#
# # 4
# #
# # Solution
# #
# # Fill out your solution below:
# #
# ___ nth_to_last_node n head
#     slow, fast _ head head
#     w___ n > 0 an. f..
#         f.. _ ?.n..
#         ? -= 1
#     __ no. f..
#         r_ h..
#     w___ ?
#         f.. _ ?.n..
#         s.. _ ?.n..
#     r_ ?
#     p..
# #
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
#     ___ test sol
#
#         a_e.. ? 2,a|,d)
#         print ('ALL TEST CASES PASSED')
#
# # Run tests
# t = TestNLast()
# t.test(nth_to_last_node)
#
# # ALL TEST CASES PASSED
