'''
Created on Oct 3, 2019

@author: tongq
'''
class Solution(object):
    ___ lenLongestFibSubseq(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        hashmap = {}
        hashset = set(A)
        ___ j __ r..(l..(A)):
            ___ i __ r..(j):
                __ A[j]-A[i] < A[i] and A[j]-A[i] __ hashset:
                    hashmap[A[i], A[j]] = hashmap.get((A[j]-A[i], A[i]), 2) + 1
        r.. max(hashmap.values() o. [0])
