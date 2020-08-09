"""
Premium Question
"""
from collections ______ defaultdict

__author__ = 'Daniel'


class TwoSum(object
    ___ __init__(self
        """
        initialize your data structure here
        """
        self.hash_map = defaultdict(int)

    ___ add(self, number
        """
        Add the number to an internal data structure.
        :rtype: nothing
        """
        self.hash_map[number] += 1

    ___ find(self, value
        """
        Find if there exists any pair of numbers which sum is equal to the value.
        :type value: int
        :rtype: bool
        """
        r_ any(
            value-k in self.hash_map and (value-k != k or self.hash_map[k] > 1)
            for k in self.hash_map
        )

    ___ find_TLE(self, value
        """
        Find if there exists any pair of numbers which sum is equal to the value.
        :type value: int
        :rtype: bool
        """
        for k in self.hash_map.keys(
            target = value - k
            __ target in self.hash_map and (target != k or self.hash_map[target] > 1
                r_ True

        r_ False
