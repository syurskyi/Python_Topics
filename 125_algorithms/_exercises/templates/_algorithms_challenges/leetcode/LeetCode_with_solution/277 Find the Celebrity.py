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


c_ Solution(object):
    ___ findCelebrity(self, n):
        """
        :type n: int
        :rtype: int
        """
        i = 0
        j = n-1
        w.... i < j:
            nxt_i, nxt_j = i, j
            __ knows(i, j) o. n.. knows(j, i):
                nxt_i += 1
            __ knows(j, i) o. n.. knows(i, j):
                nxt_j -= 1
            i, j = nxt_i, nxt_j

        celebrity = i
        ___ i __ xrange(n):
            __ i != celebrity a.. (n.. knows(i, celebrity) o. knows(celebrity, i)):
                r.. -1

        r.. celebrity

    ___ findCelebrity_set(self, n):
        """
        O(n)
        set

        :type n: int
        :rtype: int
        """
        V = set(r..(n))

        w.... l..(V) > 1:
            a = V.pop()
            b = V.pop()
            __ knows(a, b) a.. n.. knows(b, a):
                V.add(b)
            ____ n.. knows(a, b) a.. knows(b, a):
                V.add(a)

        __ n.. V:
            r.. -1

        celebrity = V.pop()
        ___ i __ xrange(n):
            __ i != celebrity a.. (n.. knows(i, celebrity) o. knows(celebrity, i)):
                r.. -1

        r.. celebrity
