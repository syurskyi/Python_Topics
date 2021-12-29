class Solution:
    """
    @param: A: an array of integer
    @param: target: An integer
    @return: an integer
    """
    ___ twoSum2(self, A, target):
        ans = 0
        __ not A or len(A) < 2:
            return ans

        A.sort()

        left, right = 0, len(A) - 1
        while left < right:
            # if minimum + maximum still <= target
            # ignore the 2nd, 3rd maximum
            __ A[left] + A[right] <= target:
                left += 1
                continue

            # if minimum + maximum > target
            # we can ensure the 2nd, 3rd minimum also fit demand
            ans += right - left
            right -= 1

        return ans
