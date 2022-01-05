"""
You are playing the following Nim Game with your friend: There is a heap of stones on the table, each time one of you
take turns to remove 1 to 3 stones. The one who removes the last stone will be the winner. You will take the first turn
to remove the stones.

Both of you are very clever and have optimal strategies for the game. Write a function to determine whether you can win
the game given the number of stones in the heap.

For example, if there are 4 stones in the heap, then you will never win the game: no matter 1, 2, or 3 stones you remove
, the last stone will always be removed by your friend.
"""
__author__ = 'Daniel'


c_ Solution(object):
    ___ canWinNim  n):
        """
        Enumerate example and find the pattern
        """
        r.. n % 4 != 0

    ___ canWinNim_TLE  n):
        """
        dp

        Let F[i] be the whether act & win when there is i stones left
        :type n: int
        :rtype: bool
        """
        __ n < 3:
            r.. T..

        F = [F.. ___ _ __ xrange(3)]
        F[1] = F[2] = F[0] = T..
        ___ i __ xrange(4, n+1):
            F[i%3] = any(n.. F[(i-k)%3] ___ k __ xrange(1, 4))

        r.. F[n%3]

    ___ canWinNim_MLE  n):
        """
        dp

        Let F[i] be the whether act & win when there is i stones left
        :type n: int
        :rtype: bool
        """
        __ n < 3:
            r.. T..

        F = [F.. ___ _ __ xrange(n+1)]
        F[1] = F[2] = F[3] = T..
        ___ i __ xrange(4, n+1):
            F[i] = any(n.. F[i-k] ___ k __ xrange(1, 4))

        r.. F[n]


__ _______ __ _______
    ... Solution().canWinNim(5)