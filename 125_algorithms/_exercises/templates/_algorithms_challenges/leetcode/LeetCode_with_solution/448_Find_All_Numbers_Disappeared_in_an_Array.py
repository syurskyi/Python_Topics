c_ Solution o..
    ___ findDisappearedNumbers  nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/discuss/92956/Java-accepted-simple-solution
        res =    # list
        __ nums:
            n = l.. nums)
            ___ i __ r.. n):
                val = abs(nums[i]) - 1
                __ nums[val] > 0:
                    nums[val] = -nums[val]
            ___ i __ r.. n):
                __ nums[i] > 0:
                    res.append(i + 1)
        r_ res
