c_ Solution:
    """
    @param: nums: an array of integers
    @param: s: An integer
    @return: an integer representing the minimum size of subarray
    """
    ___ minimumSize(self, nums, s):
        __ n.. nums o. l..(nums) __ 0:
            r.. -1
        n = l..(nums)
        min_len = n + 1
        l = r = t = 0
        w.... r < n:
            # Keep adding the next int into total until total >= s
            w.... r < n a.. t < s:
                t += nums[r]
                r += 1

            # Terminate iteration if all the children in nums have been added
            __ r >= n a.. t < s:
                break

            # Keep substracting the prev int from total until total < s
            w.... l < r a.. t >= s:
                t -= nums[l]
                l += 1

            # Save the min_size
            min_len = m..(min_len, r - l + 1)
        r.. -1 __ min_len > n ____ min_len
