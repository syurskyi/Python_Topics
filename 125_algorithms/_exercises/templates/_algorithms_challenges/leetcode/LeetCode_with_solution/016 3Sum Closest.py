"""
Given an array S of n integers, find three integers in S such that the sum is closest to a given number, target. Return
the sum of the three integers. You may assume that each input would have exactly one solution.

    For example, given array S = {-1 2 1 -4}, and target = 1.

    The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
"""
__author__ = 'Danyang'
c_ Solution:
    ___ threeSumClosest  num, target
        """
        Three pointers scanning algorithm
        Similar to 014 3Sum

        :param num: array
        :param target: target
        :return: sum of the three digits
        """
        min_distance = 1<<32
        num.s..()
        min_summation = 0

        ___ i, val __ e..(num
            j = i+1
            k = l..(num)-1
            w.... j<k:
                lst = [val, num[j], num[k]]
                __ min_distance>abs(target-s..(lst:
                    min_summation = s..(lst)
                    __ s..(lst)__target:
                        r.. min_summation
                    min_distance = abs(target-min_summation)
                ____ s..(lst)>target:
                    k -= 1
                ____:
                    j += 1
        r.. min_summation

__ _____ __ ____
    print Solution().threeSumClosest([1, 1, 1, 1], 0)

