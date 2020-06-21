# # Implement a Linked List - SOLUTION
# # Problem Statement
# # Implement a Linked List by using a Node class object. Show how you would implement a Singly Linked List and
# # a Doubly Linked List!
# # Solution
# # Since this is asking the same thing as the implementation lectures, please refer to those video lectures and notes
# # for a full explanation. The code from those lectures is displayed below:
# # Singly Linked List
# #
# c_ LinkedListNode o..
#     ___ - value
#
#         ? ?
#         nextnode _ N..
#
# a = ? 1
# b = ? 2
# c = ? 3
#
# a.nextnode = b
# b.nextnode = c
#
# # Doubly Linked List
# #
# c_ DoublyLinkedListNode o..
#
#     ___ - value
#
#         ? ?
#         next_node _ N..
#         prev_node _ N..
#
# a = ? 1
# b = ? 2
# c = ? 3
#
# # Setting b after a
# b.prev_node = a
# a.next_node = b
#
# # Setting c after a
# b.next_node = c
# c.prev_node = b
#
# # Good Job!