"""
REF: https://stackoverflow.com/questions/13093602/finding-subarray-with-maximum-sum-number-of-elements#answer-13094527

You can use binary search.

For a searched value `avg`, consider the array `B[i] = A[i] - avg`.
Now find the maximum sum subarray of length at least `k`.

This works because the average of a subarray of length `k` is

`(A[i] + ... + A[i + k - 1]) / k`.

So we have:
`(A[i] + ... + A[i + k - 1]) / k >= avg`
=> `A[i] + ... + A[i + k - 1] >= avg * k`
=> `(A[i] - avg) + ... + (A[i + k - 1] - avg) >= 0`

So, if you binary search for the average, by substracting it from each element,

if you can find a non-negative sum subarray of length at least k,
that is, find the maximum one and check if it's non-negative.

then avg is a valid answer,
continue to search in [avg, max_avg] to see if you can find a better one.
If not, reduce search to [0, avg].

       ans-2c ans-c ans ans+c ans+2c
valid    T      T    T    F     F
"""


c_ Solution:
    ___ maxAverage  nums, k
        """
        :type nums: list[int]
        :type k: int
        :rtype: float
        """
        __ n.. nums o. n.. k:
            r.. 0.0

        EPS = 1e-5

        # ans MUST between `min(nums)` and `max(nums)`
        left = right = nums[0]
        ___ num __ nums:
            __ num < left:
                left = num
            __ num > right:
                right = num

        # prefix sum
        s = [0] * (l..(nums) + 1)
        w.... right - left > EPS:
            mid = (left + right) / 2.0

            __ is_valid(nums, k, mid, s
                left = mid
            ____
                right = mid

        r.. left

    ___ is_valid  nums, k, mid, s
        s[0] = smin = 0

        ___ i __ r..(1, l..(nums) + 1
            s[i] = s[i - 1] + nums[i - 1] - mid

            __ i < k:
                _____

            """
            if there is a non-negative sum subarray of length at least k
            => it's valid even if just only one, return True immediately
            """
            __ s[i] >_ smin:  # s[i] - smin >= 0
                r.. T..

            __ s[i - k + 1] < smin:
                smin = s[i - k + 1]

        r.. F..
