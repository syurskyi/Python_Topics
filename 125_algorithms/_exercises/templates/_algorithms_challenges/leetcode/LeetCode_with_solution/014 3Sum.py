"""
Given an array S of n integers, are there elements a, b, c in S such that a + b + c = 0? Find all unique triplets in the
array which gives the sum of zero.

Note:
Elements in a triplet (a,b,c) must be in non-descending order. (ie, a <= b <= c)
The solution set must not contain duplicate triplets.
    For example, given array S = {-1 0 1 2 -1 -4},

    A solution set is:
    (-1, 0, 1)
    (-1, -1, 2)
"""
__author__ = 'Danyang'


c_ Solution:
    ___ threeSum_duplicate  num):
        """
        Hash
        O(n^2)
        :param num: array
        :return: a list of lists of length 3, [[val1,val2,val3]]
        """
        reverse_map    # dict
        ___ ind, val __ e..(num):
            __ val n.. __ reverse_map:
                reverse_map[val] = [ind]
            ____:
                reverse_map[val].a..(ind)

        result    # list
        ___ i __ x..(l..(num)):
            ___ j __ x..(i, l..(num)):
                target = 0-num[i]-num[j]
                __ target n.. __ reverse_map:
                    _____
                ___ index __ reverse_map[target]:
                    __ i != index a.. j != index:
                        result.a..([num[i], num[j], target])
                        _____
        r.. result

    ___ threeSum_TLE  num):
        """
        Hash
        O(n^2)
        :param num: array
        :return: a list of lists of length 3, [[val1,val2,val3]]
        """

        # hash
        reverse_map    # dict
        ___ ind, val __ e..(num):
            __ val n.. __ reverse_map:
                reverse_map[val] = [ind]
            ____:
                reverse_map[val].a..(ind)

        result    # dict
        ___ i __ x..(l..(num)):
            ___ j __ x..(i, l..(num)):
                target = 0-num[i]-num[j]
                __ target n.. __ reverse_map:
                    _____
                ___ index __ reverse_map[target]:
                    __ index != i a.. index != j:
                        lst = s..([num[i], num[j], target])
                        lst = t..(lst)
                        result[lst] = 1  # hash
                        _____

        r.. result.k..

    ___ threeSum  num):
        """
        Brute force first, then determine whether sorting time complexity exceeds the brute force

        Three pointers
        Algorithm:
        1. sort everything first
        2. three pointers, i, j, k
        3. notice JUMP

        Palantir Technology Interview Question

        http://en.wikipedia.org/wiki/3SUM
        O(n^2)
        Notice:
        0. duplicated element will cause "Output Limit Exceeded" error
        1. avoid using set

        :param num: array
        :return: a list of lists of length 3, [[val1,val2,val3]]
        """

        # record result
        result    # list
        num.s..()  # sorting first, avoid duplicate,
        i = 0
        w.... i < l..(num)-2:
            j = i+1
            k = l..(num)-1
            w.... j < k:
                lst = [num[i], num[j], num[k]]
                __ s..(lst) __ 0:
                    result.a..(lst)
                    k -= 1
                    j += 1
                    # JUMP remove duplicate
                    w.... j < k a.. num[j] __ num[j-1]:
                        j += 1
                    w.... j < k a.. num[k] __ num[k+1]:
                        k -= 1
                ____ s..(lst) > 0:
                    k -= 1
                ____:
                    j += 1

            i += 1
            # remove duplicate
            w.... i < l..(num)-2 a.. num[i] __ num[i-1]:
                i += 1

        r.. result


__ _______ __ _______
    print Solution().threeSum([-1, 0, 1, 2, -1, -4])