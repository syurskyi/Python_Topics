"""
Premium Question
"""
____ collections _______ defaultdict

__author__ = 'Daniel'


c_ TwoSum(object):
    ___ - ):
        """
        initialize your data structure here
        """
        hash_map = defaultdict(int)

    ___ add(self, number):
        """
        Add the number to an internal data structure.
        :rtype: nothing
        """
        hash_map[number] += 1

    ___ find(self, value):
        """
        Find if there exists any pair of numbers which sum is equal to the value.
        :type value: int
        :rtype: bool
        """
        r.. any(
            value-k __ hash_map a.. (value-k != k o. hash_map[k] > 1)
            ___ k __ hash_map
        )

    ___ find_TLE(self, value):
        """
        Find if there exists any pair of numbers which sum is equal to the value.
        :type value: int
        :rtype: bool
        """
        ___ k __ hash_map.k..:
            target = value - k
            __ target __ hash_map a.. (target != k o. hash_map[target] > 1):
                r.. T..

        r.. F..
