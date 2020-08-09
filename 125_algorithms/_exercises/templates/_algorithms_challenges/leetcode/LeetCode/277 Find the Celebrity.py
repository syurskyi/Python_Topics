"""
Premium Question
"""
__author__ = 'Daniel'


___ knows(a, b
    """
    :param a: person
    :param b: person
    :return: whether person a knows person b
    """


class Solution(object
    ___ findCelebrity(self, n
        """
        :type n: int
        :rtype: int
        """
        i = 0
        j = n-1
        w___ i < j:
            nxt_i, nxt_j = i, j
            __ knows(i, j) or not knows(j, i
                nxt_i += 1
            __ knows(j, i) or not knows(i, j
                nxt_j -= 1
            i, j = nxt_i, nxt_j

        celebrity = i
        ___ i in xrange(n
            __ i != celebrity and (not knows(i, celebrity) or knows(celebrity, i)):
                r_ -1

        r_ celebrity

    ___ findCelebrity_set(self, n
        """
        O(n)
        set

        :type n: int
        :rtype: int
        """
        V = set(range(n))

        w___ le.(V) > 1:
            a = V.pop()
            b = V.pop()
            __ knows(a, b) and not knows(b, a
                V.add(b)
            ____ not knows(a, b) and knows(b, a
                V.add(a)

        __ not V:
            r_ -1

        celebrity = V.pop()
        ___ i in xrange(n
            __ i != celebrity and (not knows(i, celebrity) or knows(celebrity, i)):
                r_ -1

        r_ celebrity
