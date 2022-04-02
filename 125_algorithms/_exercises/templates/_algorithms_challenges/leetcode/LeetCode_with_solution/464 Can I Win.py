#!/usr/bin/python3
"""
In the "100 game," two players take turns adding, to a running total, any
integer from 1..10. The player who first causes the running total to reach or
exceed 100 wins.

What if we change the game so that players cannot re-use integers?

For example, two players might take turns drawing from a common pool of numbers
of 1..15 without replacement until they reach a total >= 100.

Given an integer maxChoosableInteger and another integer desiredTotal, determine
if the first player to move can force a win, assuming both players play
optimally.

You can always assume that maxChoosableInteger will not be larger than 20 and
desiredTotal will not be larger than 300.
"""


c_ Solution:
    ___ canIWin  maxChoosableInteger, desiredTotal
        """
        can p win?
        F^p_{total, choice_set - i} = not any(
            F^p'_{total - A[j] - A[i], choice_set - j - i}
            for j
        )

        :type maxChoosableInteger: int
        :type desiredTotal: int
        :rtype: bool
        """
        cache    # dict
        # set is not hashable while frozenset is
        c.. = frozenset([choice ___ choice __ r..(1, maxChoosableInteger + 1)])
        r.. _can_win(desiredTotal, c.., s..(c..), cache)

    ___ _can_win  total, c.., gross,cache
        __ (total, c..) __ cache:
            r.. cache[(total, c..)]

        ret = F..
        __ m..(c..) >= total:
            ret = T..

        ____ gross < total:
            ret = F..
        ____:
            ___ choice __ c..:
                __ n.. _can_win(
                        total - choice,
                        c.. - s..([choice]),
                        gross - choice,
                        cache

                    ret = T..
                    _____

        cache[(total, c..)] = ret
        r.. ret


__ _______ __ _______
    ... Solution().canIWin(10, 11) __ F..
    ... Solution().canIWin(10, 0) __ T..
    ... Solution().canIWin(13, 11) __ T..
