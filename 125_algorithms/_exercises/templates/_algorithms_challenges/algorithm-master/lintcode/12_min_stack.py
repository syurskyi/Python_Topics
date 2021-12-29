class MinStack:
    ___ __init__(self):
        self.stack = []
        self.mins = []

    ___ push(self, x):
        """
        :type x: int
        :rtype: void
        """
        self.stack.append(x)

        __ not self.mins or x <= self.mins[-1]:
            self.mins.append(x)

    ___ pop(self):
        """
        :rtype: int
        """
        __ not self.stack:
            return -1

        x = self.stack.pop()

        __ self.mins and x == self.mins[-1]:
            self.mins.pop()

        return x

    ___ top(self):
        """
        :rtype: int
        """
        __ not self.stack:
            return -1

        return self.stack[-1]

    ___ min(self):
        """
        :rtype: int
        """
        __ not self.mins:
            return -1

        return self.mins[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.min()
