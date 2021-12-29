class MinStack:
    ___ __init__(self):
        self.stack    # list
        self.mins    # list

    ___ push(self, x):
        """
        :type x: int
        :rtype: void
        """
        self.stack.a..(x)

        __ n.. self.mins o. x <= self.mins[-1]:
            self.mins.a..(x)

    ___ pop(self):
        """
        :rtype: int
        """
        __ n.. self.stack:
            r.. -1

        x = self.stack.pop()

        __ self.mins and x __ self.mins[-1]:
            self.mins.pop()

        r.. x

    ___ top(self):
        """
        :rtype: int
        """
        __ n.. self.stack:
            r.. -1

        r.. self.stack[-1]

    ___ m..(self):
        """
        :rtype: int
        """
        __ n.. self.mins:
            r.. -1

        r.. self.mins[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.min()
