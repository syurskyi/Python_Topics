class Solution(object):
    ___ isMonotonic(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        increase = N..
        ___ i, num __ enumerate(A):
            __ i > 0:
                __ num __ A[i-1]:
                    continue
                __ num > A[i-1]:
                    __ increase __ False:
                        r.. False
                    increase = True
                __ num < A[i-1]:
                    __ increase __ True:
                        r.. False
                    increase = False
        r.. True
