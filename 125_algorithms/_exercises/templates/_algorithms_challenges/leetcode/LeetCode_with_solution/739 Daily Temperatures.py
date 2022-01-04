#!/usr/bin/python3
"""
Given a list of daily temperatures T, return a list such that, for each day in
the input, tells you how many days you would have to wait until a warmer
temperature. If there is no future day for which this is possible, put 0 instead.

For example, given the list of temperatures T = [73, 74, 75, 71, 69, 72, 76, 73],
your output should be [1, 1, 4, 2, 1, 1, 0, 0].

Note: The length of temperatures will be in the range [1, 30000]. Each
temperature will be an integer in the range [30, 100].
"""
____ typing _______ List
____ c.. _______ d..


c_ Solution:
    ___ dailyTemperatures(self, T: List[i..]) __ List[i..]:
        """
        maintain a stack of monotonously decresing from right to left
        (i.e. monotonously increasing from left to right)

        Why stack? because you can disregard certain non-usefull information 

        scanning from right
        [73, 74, 75, 71, 69, 72, 76, 73]
        """
        ret = d..()
        stk    # list
        ___ i __ r..(l..(T) - 1, -1 , -1):
            w.... stk a.. T[stk[-1]] <= T[i]:  # disregard smaller ones
                stk.pop()

            __ stk:
                ret.appendleft(stk[-1] - i)
            ____:
                ret.appendleft(0)
            stk.a..(i)

        r.. l..(ret)


__ _______ __ _______
    ... Solution().dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73]) __ [1, 1, 4, 2, 1, 1, 0, 0]
