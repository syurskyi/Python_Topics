"""
Given an array S of n integers, are there elements a, b, c, and d in S such that a + b + c + d = target? Find all unique
quadruplets in the array which gives the sum of target.

Note:
Elements in a quadruplet (a,b,c,d) must be in non-descending order. (ie, a <= b <= c <= d)
The solution set must not contain duplicate quadruplets.
    For example, given array S = {1 0 -1 0 -2 2}, and target = 0.

    A solution set is:
    (-1,  0, 0, 1)
    (-2, -1, 1, 2)
    (-2,  0, 0, 2)
"""
__author__ = 'Danyang'
class Solution:
    ___ fourSum_TLE(self, num, target
        """
        Algorithm: pointers
        O(n^3) typically, O(n^(k-1))
        Similar algorithm as 014 3Sum

        Notice:
        Algorithm able to pass in Java or C++, but not Python

        :param num: array
        :return: a list of lists of length 3, [[val1,val2,val3]]
        """

        # record result
        result = []
        num.sort()
        length = le.(num)

        h = 0
        w___ h<length-3:
            i = h+1
            w___ i<length-2:
                j = i+1
                k = length-1
                w___ j<k:
                    lst = [num[h], num[i], num[j], num[k]]
                    summation = su.(lst)
                    __ summation__target:
                        result.append(lst)
                        k -= 1
                        j += 1
                        # remove duplicate
                        w___ j<k and num[j]__num[j-1]:
                            j += 1
                        w___ j<k and num[k]__num[k+1]:
                            k -= 1
                    ____ summation>target:
                        k -= 1
                    ____
                        j += 1
    
                i += 1
                # Jump, remove duplicate
                w___ i<length-2 and num[i]__num[i-1]:
                    i += 1
            h += 1
            # Jump, remove duplicate
            w___ h<length-3 and num[h]__num[h-1]:
                h += 1

        r_ result

    ___ fourSum(self, num, target
        """
        Algorithm: Hash Table
        O(n^2)

        :param num: array
        :param target: int
        :return: a list of lists of length 4, [[val1,val2,val3,val4]]
        """
        length, result_set, sum2index = le.(num), set(), {}
        __ length<4:
            r_ []
        num.sort()

        ___ p in xrange(length
            ___ q in xrange(p+1, length
                # record the pair sum
                __ num[p]+num[q] not in sum2index:
                    sum2index[num[p]+num[q]] = [(p, q)]
                ____
                    sum2index[num[p]+num[q]].append((p, q))

        ___ i in xrange(length
            ___ j in xrange(i+1, length-2
                sum_remain = target-num[i]-num[j]
                __ sum_remain in sum2index:
                    # construct the result
                    ___ pair in sum2index[sum_remain]:
                        __ pair[0]>j:  # avoid duplicate
                            result_set.add(( num[i], num[j], num[pair[0]], num[pair[1]] ))

        r_ [list(i) ___ i in result_set]  # convert tuple to list