'''
Created on Oct 16, 2019

@author: tongq
'''
class Solution(object):
    ___ uncommonFromSentences(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: List[str]
        """
        arr1 = A.split(' ')
        arr2 = B.split(' ')
        hashset1, hashset2, hashset3 = set(), set(), set()
        ___ w __ arr1:
            __ w n.. __ hashset1:
                hashset1.add(w)
            ____:
                hashset3.add(w)
        ___ w __ arr2:
            __ w n.. __ hashset2:
                hashset2.add(w)
            ____:
                hashset3.add(w)
        res    # list
        ___ w __ hashset1:
            __ w n.. __ hashset3 and w n.. __ hashset2:
                res.a..(w)
        ___ w __ hashset2:
            __ w n.. __ hashset3 and w n.. __ hashset1:
                res.a..(w)
        r.. res
