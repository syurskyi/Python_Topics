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


class Solution:
    ___ threeSum_duplicate(self, num
        """
        Hash
        O(n^2)
        :param num: array
        :return: a list of lists of length 3, [[val1,val2,val3]]
        """
        reverse_map = {}
        ___ ind, val in enumerate(num
            __ val not in reverse_map:
                reverse_map[val] = [ind]
            ____
                reverse_map[val].append(ind)

        result = []
        ___ i in xrange(le.(num)):
            ___ j in xrange(i, le.(num)):
                target = 0-num[i]-num[j]
                __ target not in reverse_map:
                    continue
                ___ index in reverse_map[target]:
                    __ i != index and j != index:
                        result.append([num[i], num[j], target])
                        break
        r_ result

    ___ threeSum_TLE(self, num
        """
        Hash
        O(n^2)
        :param num: array
        :return: a list of lists of length 3, [[val1,val2,val3]]
        """

        # hash
        reverse_map = {}
        ___ ind, val in enumerate(num
            __ val not in reverse_map:
                reverse_map[val] = [ind]
            ____
                reverse_map[val].append(ind)

        result = {}
        ___ i in xrange(le.(num)):
            ___ j in xrange(i, le.(num)):
                target = 0-num[i]-num[j]
                __ target not in reverse_map:
                    continue
                ___ index in reverse_map[target]:
                    __ index != i and index != j:
                        lst = sorted([num[i], num[j], target])
                        lst = tuple(lst)
                        result[lst] = 1  # hash
                        break

        r_ result.keys()

    ___ threeSum(self, num
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
        result = []
        num.sort()  # sorting first, avoid duplicate,
        i = 0
        w___ i < le.(num)-2:
            j = i+1
            k = le.(num)-1
            w___ j < k:
                lst = [num[i], num[j], num[k]]
                __ su.(lst) __ 0:
                    result.append(lst)
                    k -= 1
                    j += 1
                    # JUMP remove duplicate
                    w___ j < k and num[j] __ num[j-1]:
                        j += 1
                    w___ j < k and num[k] __ num[k+1]:
                        k -= 1
                ____ su.(lst) > 0:
                    k -= 1
                ____
                    j += 1

            i += 1
            # remove duplicate
            w___ i < le.(num)-2 and num[i] __ num[i-1]:
                i += 1

        r_ result


__ __name__ __ "__main__":
    print Solution().threeSum([-1, 0, 1, 2, -1, -4])