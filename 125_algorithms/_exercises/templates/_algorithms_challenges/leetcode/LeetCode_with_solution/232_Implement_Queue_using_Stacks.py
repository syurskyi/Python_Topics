# class Queue(object):
#     def __init__(self):
#         """
#         initialize your data structure here.
#         """
#         self.stack1 = []
#         self.stack2 = []
#
#
#     def push(self, x):
#         """
#         :type x: int
#         :rtype: nothing
#         """
#         while len(self.stack1) > 0:
#             curr = self.stack1.pop()
#             self.stack2.append(curr)
#         self.stack1.append(x)
#         while len(self.stack2) > 0:
#             curr = self.stack2.pop()
#             self.stack1.append(curr)
#
#     def pop(self):
#         """
#         :rtype: nothing
#         """
#         self.stack1.pop()
#
#
#     def peek(self):
#         """
#         :rtype: int
#         """
#         return self.stack1[-1]
#
#     def empty(self):
#         """
#         :rtype: bool
#         """
#         return len(self.stack1) == 0

c_ Queue o..
    ___ -(self):
        """
        initialize your data structure here.
        """
        stack1 = []
        stack2 = []


    ___ push  x):
        """
        :type x: int
        :rtype: nothing
        """
        stack1.append(x)

    ___ pop(self):
        """
        :rtype: nothing
        """
        __ l.. stack2) __ 0:
            w.. l.. stack1):
                curr = stack1.pop()
                stack2.append(curr)
        stack2.pop()


    ___ peek(self):
        """
        :rtype: int
        """
        __ l.. stack2) __ 0:
            w.. l.. stack1):
                curr = stack1.pop()
                stack2.append(curr)
        r_ stack2[-1]

    ___ empty(self):
        """
        :rtype: bool
        """
        r_ l.. stack1) + l.. stack2) __ 0