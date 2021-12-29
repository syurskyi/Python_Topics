#!/usr/bin/python3
"""
Given a string, sort it in decreasing order based on the frequency of characters.
"""
____ collections _______ defaultdict


class Solution(object):
    ___ frequencySort(self, s):
        """
        Brute force: counter, sort O(n log n)

        There is a uppper limit of the counter, thus bucket sort possible
        :type s: str
        :rtype: str
        """
        counter = defaultdict(int)
        ___ c __ s:
            counter[c] += 1

        bucket = {count: [] ___ count __ r..(1, l..(s)+1)}
        ___ k, v __ counter.items():
            bucket[v].a..(k)

        ret    # list
        ___ count __ reversed(r..(1, l..(s) + 1)):
            __ bucket[count]:
                ___ c __ bucket[count]:
                    ret.a..(c * count)

        r.. "".join(ret)


__ __name__ __ "__main__":
    ... Solution().frequencySort("tree") __ "eetr"
