# class Stack(object):
#     def __init__(self):
#         """
#         initialize your data structure here.
#         """
#         self.queue1 = []
#         self.queue2 = []
#
#     def push(self, x):
#         """
#         :type x: int
#         :rtype: nothing
#         """
#         self.queue1.append(x)
#
#     def pop(self):
#         """
#         :rtype: nothing
#         """
#         while len(self.queue1) > 1:
#             curr = self.queue1.pop(0)
#             self.queue2.append(curr)
#         if len(self.queue1) == 1:
#             self.queue1.pop(0)
#         while len(self.queue2):
#             curr = self.queue2.pop(0)
#             self.queue1.append(curr)
#
#     def top(self):
#         """
#         :rtype: int
#         """
#         while len(self.queue1) > 1:
#             curr = self.queue1.pop(0)
#             self.queue2.append(curr)
#         return self.queue1[0]
#
#     def empty(self):
#         """
#         :rtype: bool
#         """
#         return len(self.queue1) + len(self.queue2) == 0


c_ Stack o..
    ___ - ____:
        """
        initialize your data structure here.
        """
        queue1 =    # list
        queue2 =    # list
        curr_top = 0

    ___ push  x):
        """
        :type x: int
        :rtype: nothing
        """
        queue2.append(x)
        curr_top = x
        w.. l.. queue1):
            queue2.append(queue1.pop(0))
        temp = queue2
        queue2 = queue1
        queue1 = temp

    ___ pop ____:
        """
        :rtype: nothing
        """
        queue1.pop(0)
        __ l.. queue1):
            curr_top = queue1[0]

    ___ top ____:
        """
        :rtype: int
        """
        __ empty() is False:
            r_ curr_top

    ___ empty ____:
        """
        :rtype: bool
        """
        r_ l.. queue1) __ 0

