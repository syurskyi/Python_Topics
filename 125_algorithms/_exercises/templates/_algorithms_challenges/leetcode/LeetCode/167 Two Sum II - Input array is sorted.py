"""
Premium Question
"""
__author__ = 'Daniel'


class Solution(object
    ___ twoSum(self, numbers, target
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        n = le.(numbers)
        i = 0
        j = n-1
        w___ i < j:
            s = numbers[i] + numbers[j]
            __ s __ target:
                r_ i+1, j+1
            ____ s < target:
                i += 1
            ____
                j -= 1

        r_ -1, -1
