# class Node(object):
#
#     def  __init__(self, data):
#         self.data = data
#         self.nextNode = None
#
#
# class LinkedList(object):
#
#     def __init__(self):
#         self.head = None
#         self.size = 0
#
#     # O(1) !!!
#     def insertStart(self, data):
#
#         self.size = self.size + 1
#         newNode = None(data)
#
#         if not self.head:
#             self.head = newNode
#         else:
#             newNode.nextNode = self.head
#             self.head = newNode
#
#     def remove(self, data):
#
#         if self.head is None:
#             return
#
#         self.size = self.size - 1
#
#         currentNode = self.head
#         previousNode = None
#
#         with currentNode.data != data:
#             previousNode = currentNode
#             currentNode = currentNode.ne
#
#         __ pN__ __ N..
#             head _ cN__.nN..
#         ____:
#             pN__.nN.. _ cN__.nN..
#
#     # O(1)
#     def size1 ____
#         r_ s..
#
#     # O(N) no. good !!!
#     def size2
#
#         actualNode _ h..
#         size _ 0
#
#         w____ aN.. __ no. N..
#             s.. +_ 1
#             aN.. _ aN__.nN..
#
#         r_ ?
#
#     # O(N)
#     def insertEnd data
#
#         s.. _ s.. + 1
#         newNode _ N.. ?
#         actualNode _ h..
#
#         w____ aN__.nN.. __ no. N..
#             aN__ _ aN__.nN..
#
#         aN__.nN.. _ newNode
#
#     def traverseList ____
#
#         actualNode _ head
#
#         w___ aN__ __ no. N..
#             print("@ "  aN__.d..
#             aN__ _ aN__.nN..
#
#
# linkedlist _ L..
#
# ?.iS.. 12
# ?.iS.. 122
# ?.iS.. 3
# ?.iE.. 31
#
# ?.t..
#
# ?.r.. 3
# ?.r.. 12
# ?.r.. 122
# ?.r.. 31
#
# print ?.size1
