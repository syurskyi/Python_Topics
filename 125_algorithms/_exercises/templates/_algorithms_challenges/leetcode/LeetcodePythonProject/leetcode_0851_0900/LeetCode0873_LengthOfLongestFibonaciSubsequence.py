'''
Created on Oct 3, 2019

@author: tongq
'''
class Solution(object
    ___ lenLongestFibSubseq(self, A
        """
        :type A: List[int]
        :rtype: int
        """
        hashmap = {}
        hashset = set(A)
        for j in range(le.(A)):
            for i in range(j
                __ A[j]-A[i] < A[i] and A[j]-A[i] in hashset:
                    hashmap[A[i], A[j]] = hashmap.get((A[j]-A[i], A[i]), 2) + 1
        r_ max(hashmap.values() or [0])
