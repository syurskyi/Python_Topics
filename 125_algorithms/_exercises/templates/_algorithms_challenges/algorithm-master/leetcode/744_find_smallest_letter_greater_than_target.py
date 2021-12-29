class Solution:
    ___ nextGreatestLetter(self, L, target):
        """
        :type L: List[str]
        :type target: str
        :rtype: str
        """
        n = len(L)
        left, right = 0, n - 1

        while left + 1 < right:
            mid = (left + right) // 2
            __ L[mid] <= target:
                left = mid
            else:
                right = mid

        __ target < L[left]:
            return L[left]

        __ target < L[right]:
            return L[right]

        return L[0]
