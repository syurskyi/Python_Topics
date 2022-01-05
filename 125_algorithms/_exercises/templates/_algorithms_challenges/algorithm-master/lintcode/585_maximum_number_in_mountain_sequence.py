c_ Solution:
    """
    @param: nums: a mountain sequence which increase firstly and then decrease
    @return: then mountain top
    """
    ___ mountainSequence  nums):
        __ n.. nums:
            r.. -1

        l, m, r = 0, 0, l..(nums) - 1

        w.... l + 1 < r:
            m = l + (r - l) // 2
            """
            `m+1` will not out of range
            if len(nums) == 1 || 2, the code in this loop will not execute
            """
            __ nums[m] > nums[m+1]:
                r = m
            ____:
                l = m

        r.. m..(nums[l], nums[r])
