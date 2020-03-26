# # Singly Linked List Cycle Check - SOLUTION
# # Problem
# # Given a singly linked list, write a function which takes in the first node in a singly linked list and returns
# # a boolean indicating if the linked list contains a "cycle".
# # A cycle is when a node's next point actually points back to a previous node in the list. This is also sometimes known
# # as a circularly linked list.
#
# # You've been given the Linked List Node class code:
#
# c_ Node o..
#
#     ___ - value
#
#         ? ?
#         nextnode _ N..
#
# # Solution
# # To solve this problem we will have two markers traversing through the list. marker1 and marker2. We will have
# # both makers begin at the first node of the list and traverse through the linked list. However the second marker,
# # marker2, will move two nodes ahead for every one node that marker1 moves.
# # By this logic we can imagine that the markers are "racing" through the linked list, with marker2 moving faster.
# # If the linked list has a cylce and is circularly connected we will have the analogy of a track, in this case
# # the marker2 will eventually be "lapping" the marker1 and they will equal each other.
# # If the linked list has no cycle, then marker2 should be able to continue on until the very end, never equaling
# # the first marker.
# #
# # Let's see this logic coded out:
#
# ___ cycle_check node
#
#     # Begin both markers at the first node
#     marker1 _ ?
#     marker2 _ ?
#
#     # Go until end of list
#     w___ _2 !_ N.. an. _2.n.. !_ N..
#
#         # Note
#         _1 _ _1.n..
#         _2 _ _2.n__.n__
#
#         # Check if the markers have matched
#         __ _2 __ _1
#             r_ T..
#
#     # Case where marker ahead reaches the end of the list
#     r_ F..
#
# # Test Your Solution
# #
# # """
# # RUN THIS CELL TO TEST YOUR SOLUTION
# # """
# from nose.tools import assert_equal
# #
# # CREATE CYCLE LIST
# a = Node(1)
# b = Node(2)
# c = Node(3)
#
# a.nextnode = b
# b.nextnode = c
# c.nextnode = a # Cycle Here!
#
#
# # CREATE NON CYCLE LIST
# x = Node(1)
# y = Node(2)
# z = Node(3)
#
# x.nextnode = y
# y.nextnode = z
#
#
# # #############
# c_ TestCycleCheck o..
#
#     ___ test sol
#         a_e.. ?(a),T..
#         a_e.. ?(x),F..
#
#         print "ALL TEST CASES PASSED"
#
# # Run Tests
#
# t = TestCycleCheck()
# t.test(cycle_check)
#
# # ALL TEST CASES PASSED
# #
# # Good Job!