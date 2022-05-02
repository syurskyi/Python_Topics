# class MinStack(object):
#     def __init__(self):
#         """
#         initialize your data structure here.
#         """
#         self.stack = []
#         self.min_stack = []


#     def push(self, x):
#         """
#         :type x: int
#         :rtype: nothing
#         """
#         self.stack.append(x)
#         if len(self.min_stack) == 0 or x <= self.min_stack[-1]:
#             self.min_stack.append(x)


#     def pop(self):
#         """
#         :rtype: nothing
#         """
#         if len(self.stack) > 0:
#             last = self.stack[-1]
#             # Need to check whether pop minStack
#             if len(self.min_stack) > 0 and last == self.min_stack[-1]:
#                 self.min_stack.pop()
#             self.stack.pop()


#     def top(self):
#         """
#         :rtype: int
#         """
#         if len(self.stack) > 0:
#             return self.stack[-1]
#         return None


#     def getMin(self):
#         """
#         :rtype: int
#         """
#         if len(self.min_stack) > 0:
#             return self.min_stack[-1]
#         else:
#             if len(self.stack) > 0:
#                 return self.stack[-1]
#             return None

c_ MinStack o..
    ___ -(self):
        """
        initialize your data structure here.
        """
        stack =    # list
        min_stack =    # list


    ___ push  x):
        """
        :type x: int
        :rtype: nothing
        """
        stack.append(x)
        __ l.. min_stack) __ 0:
            min_stack.append(x)
            r_
        __ x <= min_stack[-1]:
            min_stack.append(x)
        ____
            # Push top of min stack again
            min_stack.append(min_stack[-1])


    ___ pop(self):
        """
        :rtype: nothing
        """
        __ l.. stack) > 0:
            # Much simple than solution 1
            # But use more space
            min_stack.pop()
            stack.pop()


    ___ top(self):
        """
        :rtype: int
        """
        __ l.. stack) > 0:
            r_ stack[-1]
        r_ N..


    ___ getMin(self):
        """
        :rtype: int
        """
        __ l.. min_stack) > 0:
            r_ min_stack[-1]
        r_ N..
