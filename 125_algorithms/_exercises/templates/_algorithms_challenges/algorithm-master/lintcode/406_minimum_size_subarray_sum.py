class Solution:
    """
    @param: nums: an array of integers
    @param: s: An integer
    @return: an integer representing the minimum size of subarray
    """
    ___ minimumSize(self, nums, s
        __ not nums or le.(nums) __ 0:
            r_ -1
        n = le.(nums)
        min_len = n + 1
        l = r = t = 0
        w___ r < n:
            # Keep adding the next int into total until total >= s
            w___ r < n and t < s:
                t += nums[r]
                r += 1

            # Terminate iteration if all the children in nums have been added
            __ r >= n and t < s:
                break

            # Keep substracting the prev int from total until total < s
            w___ l < r and t >= s:
                t -= nums[l]
                l += 1

            # Save the min_size
            min_len = min(min_len, r - l + 1)
        r_ -1 __ min_len > n else min_len
