c_ Solution o..
    ___ firstMissingPositive  nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # https://leetcode.com/discuss/86025/java-clean-o-n-solution-with-explanation
        ls = l.. nums)
        index = 0
        w.. index < ls:
            # nums[nums[index] - 1] == nums[index] means that the num is in right position
            __ nums[index] <= 0 or nums[index] > ls or nums[nums[index] - 1] __ nums[index]:
                index += 1
            ____
                # swap current num to correct position
                pos = nums[index] - 1
                nums[index], nums[pos] = nums[pos], nums[index]
        res = 0
        w.. res < ls and nums[res] __ res + 1:
            res += 1
        r_ res + 1
