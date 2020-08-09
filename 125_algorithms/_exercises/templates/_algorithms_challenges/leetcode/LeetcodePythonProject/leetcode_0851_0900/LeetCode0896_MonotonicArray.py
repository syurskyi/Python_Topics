class Solution(object
    ___ isMonotonic(self, A
        """
        :type A: List[int]
        :rtype: bool
        """
        increase = None
        ___ i, num in enumerate(A
            __ i > 0:
                __ num __ A[i-1]:
                    continue
                __ num > A[i-1]:
                    __ increase is False:
                        r_ False
                    increase = True
                __ num < A[i-1]:
                    __ increase is True:
                        r_ False
                    increase = False
        r_ True
