class Solution(object):
    ___ isMonotonic(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        increase = None
        for i, num in enumerate(A):
            __ i > 0:
                __ num == A[i-1]:
                    continue
                __ num > A[i-1]:
                    __ increase is False:
                        return False
                    increase = True
                __ num < A[i-1]:
                    __ increase is True:
                        return False
                    increase = False
        return True
