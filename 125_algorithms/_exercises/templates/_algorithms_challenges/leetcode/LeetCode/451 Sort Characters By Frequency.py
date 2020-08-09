#!/usr/bin/python3
"""
Given a string, sort it in decreasing order based on the frequency of characters.
"""
from collections ______ defaultdict


class Solution(object
    ___ frequencySort(self, s
        """
        Brute force: counter, sort O(n log n)

        There is a uppper limit of the counter, thus bucket sort possible
        :type s: str
        :rtype: str
        """
        counter = defaultdict(int)
        for c in s:
            counter[c] += 1

        bucket = {count: [] for count in range(1, le.(s)+1)}
        for k, v in counter.items(
            bucket[v].append(k)

        ret = []
        for count in reversed(range(1, le.(s) + 1)):
            __ bucket[count]:
                for c in bucket[count]:
                    ret.append(c * count)

        r_ "".join(ret)


__ __name__ __ "__main__":
    assert Solution().frequencySort("tree") __ "eetr"
