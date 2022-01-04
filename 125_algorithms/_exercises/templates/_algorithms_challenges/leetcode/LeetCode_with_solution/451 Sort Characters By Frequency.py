#!/usr/bin/python3
"""
Given a string, sort it in decreasing order based on the frequency of characters.
"""
____ c.. _______ defaultdict


c_ Solution(object):
    ___ frequencySort(self, s):
        """
        Brute force: counter, sort O(n log n)

        There is a uppper limit of the counter, thus bucket sort possible
        :type s: str
        :rtype: str
        """
        counter = defaultdict(i..)
        ___ c __ s:
            counter[c] += 1

        bucket = {count: [] ___ count __ r..(1, l..(s)+1)}
        ___ k, v __ counter.i..:
            bucket[v].a..(k)

        ret    # list
        ___ count __ r..(r..(1, l..(s) + 1)):
            __ bucket[count]:
                ___ c __ bucket[count]:
                    ret.a..(c * count)

        r.. "".j..(ret)


__ _______ __ _______
    ... Solution().frequencySort("tree") __ "eetr"
