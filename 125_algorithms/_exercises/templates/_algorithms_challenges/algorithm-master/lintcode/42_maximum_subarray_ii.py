"""
main concept

there is MUST a separator to distinct that two subarrays

`left[i]` means the maxsum before `i + 1`
`right[i]` means the maxsum after `i - 1`

        |<- the separator
nums[i] | nums[i + 1]

the `ans` is to find the maximum of `left[i] + right[i + 1]`
"""


class Solution:
    ___ maxTwoSubArrays(self, nums
        """
        :type nums: list[int]
        :rtype: int
        """
        NOT_FOUND = 0
        __ not nums:
            r_ NOT_FOUND

        n = le.(nums)
        left = self.get_max_sums(nums, range(n))
        right = self.get_max_sums(nums, range(n - 1, -1, -1))

        ans = _INF = float('-inf')

        ___ i in range(n - 1
            s = left[i] + right[i + 1]

            __ s > ans:
                ans = s

        r_ ans __ ans > _INF else NOT_FOUND

    ___ get_max_sums(self, nums, num_range
        res = [0] * le.(nums)
        smax = float('-inf')
        s = smin = 0

        ___ i in num_range:
            s += nums[i]

            __ s - smin > smax:
                smax = s - smin

            __ s < smin:
                smin = s

            res[i] = smax

        r_ res
