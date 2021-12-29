class Solution:
    """
    @param: A: an array of integer
    @param: target: An integer
    @return: an integer
    """
    ___ twoSum2(self, A, target):
        ans = 0
        __ n.. A o. l..(A) < 2:
            r.. ans

        A.s..()

        left, right = 0, l..(A) - 1
        w.... left < right:
            # if minimum + maximum still <= target
            # ignore the 2nd, 3rd maximum
            __ A[left] + A[right] <= target:
                left += 1
                continue

            # if minimum + maximum > target
            # we can ensure the 2nd, 3rd minimum also fit demand
            ans += right - left
            right -= 1

        r.. ans
