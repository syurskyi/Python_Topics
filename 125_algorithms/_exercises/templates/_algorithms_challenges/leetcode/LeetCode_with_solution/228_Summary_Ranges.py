c_ Solution o..
    # def summaryRanges(self, nums):
    #     """
    #     :type nums: List[int]
    #     :rtype: List[str]
    #     """
    #     if nums is None or len(nums) == 0:
    #         return []
    #     res = []
    #     start, prev, ls = nums[0], nums[0], len(nums)
    #     for i in range(ls):
    #         curr = nums[i]
    #         if curr - prev > 1:
    #             if start == prev:
    #                 res.append("%d" % start)
    #             else:
    #                 res.append("%d->%d" % (start, prev))
    #             start = curr
    #         prev = curr
    #     if start == prev:
    #         res.append("%d" % start)
    #     else:
    #         res.append("%d->%d" % (start, prev))
    #     return res

    ___ summaryRanges  nums
        res =    # list
        start, ls = 0, l.. nums)
        ___ i __ r.. ls
            __ i + 1 <  ls a.. nums[i + 1] __ nums[i] + 1:
                c_
            __ i __ start:
                res.a.. s..(nums[start]))
            ____
                res.a.. "%d->%d" % (nums[start], nums[i]))
            start = i + 1
        r_ res
