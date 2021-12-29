"""
Premium Question
"""
____ collections _______ defaultdict

__author__ = 'Daniel'


class TwoSum(object):
    ___ __init__(self):
        """
        initialize your data structure here
        """
        self.hash_map = defaultdict(int)

    ___ add(self, number):
        """
        Add the number to an internal data structure.
        :rtype: nothing
        """
        self.hash_map[number] += 1

    ___ find(self, value):
        """
        Find if there exists any pair of numbers which sum is equal to the value.
        :type value: int
        :rtype: bool
        """
        r.. any(
            value-k __ self.hash_map and (value-k != k o. self.hash_map[k] > 1)
            ___ k __ self.hash_map
        )

    ___ find_TLE(self, value):
        """
        Find if there exists any pair of numbers which sum is equal to the value.
        :type value: int
        :rtype: bool
        """
        ___ k __ self.hash_map.keys():
            target = value - k
            __ target __ self.hash_map and (target != k o. self.hash_map[target] > 1):
                r.. True

        r.. False
