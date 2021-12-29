"""
Premium Question
"""
__author__ = 'Daniel'


___ knows(a, b):
    """
    :param a: person
    :param b: person
    :return: whether person a knows person b
    """


class Solution(object):
    ___ findCelebrity(self, n):
        """
        :type n: int
        :rtype: int
        """
        i = 0
        j = n-1
        while i < j:
            nxt_i, nxt_j = i, j
            __ knows(i, j) or not knows(j, i):
                nxt_i += 1
            __ knows(j, i) or not knows(i, j):
                nxt_j -= 1
            i, j = nxt_i, nxt_j

        celebrity = i
        for i in xrange(n):
            __ i != celebrity and (not knows(i, celebrity) or knows(celebrity, i)):
                return -1

        return celebrity

    ___ findCelebrity_set(self, n):
        """
        O(n)
        set

        :type n: int
        :rtype: int
        """
        V = set(range(n))

        while len(V) > 1:
            a = V.pop()
            b = V.pop()
            __ knows(a, b) and not knows(b, a):
                V.add(b)
            elif not knows(a, b) and knows(b, a):
                V.add(a)

        __ not V:
            return -1

        celebrity = V.pop()
        for i in xrange(n):
            __ i != celebrity and (not knows(i, celebrity) or knows(celebrity, i)):
                return -1

        return celebrity
