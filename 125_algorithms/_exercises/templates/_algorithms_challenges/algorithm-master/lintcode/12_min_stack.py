c_ MinStack:
    ___ -
        stack    # list
        mins    # list

    ___ push  x
        """
        :type x: int
        :rtype: void
        """
        stack.a..(x)

        __ n.. mins o. x <_ mins[-1]:
            mins.a..(x)

    ___ pop
        """
        :rtype: int
        """
        __ n.. stack:
            r.. -1

        x = stack.p.. )

        __ mins a.. x __ mins[-1]:
            mins.p.. )

        r.. x

    ___ top
        """
        :rtype: int
        """
        __ n.. stack:
            r.. -1

        r.. stack[-1]

    ___ m..
        """
        :rtype: int
        """
        __ n.. mins:
            r.. -1

        r.. mins[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.min()
