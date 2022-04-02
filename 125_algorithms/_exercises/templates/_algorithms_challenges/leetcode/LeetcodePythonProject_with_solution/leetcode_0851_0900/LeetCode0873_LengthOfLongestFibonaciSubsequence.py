'''
Created on Oct 3, 2019

@author: tongq
'''
c_ Solution(o..
    ___ lenLongestFibSubseq  A
        """
        :type A: List[int]
        :rtype: int
        """
        hashmap    # dict
        hashset = s..(A)
        ___ j __ r..(l..(A)):
            ___ i __ r..(j
                __ A[j]-A[i] < A[i] a.. A[j]-A[i] __ hashset:
                    hashmap[A[i], A[j]] = hashmap.get((A[j]-A[i], A[i]), 2) + 1
        r.. m..(hashmap.v.. o. [0])
