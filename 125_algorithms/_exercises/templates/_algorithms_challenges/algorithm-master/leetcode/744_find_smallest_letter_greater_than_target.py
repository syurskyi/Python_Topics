c_ Solution:
    ___ nextGreatestLetter(self, L, target):
        """
        :type L: List[str]
        :type target: str
        :rtype: str
        """
        n = l..(L)
        left, right = 0, n - 1

        w.... left + 1 < right:
            mid = (left + right) // 2
            __ L[mid] <= target:
                left = mid
            ____:
                right = mid

        __ target < L[left]:
            r.. L[left]

        __ target < L[right]:
            r.. L[right]

        r.. L[0]
