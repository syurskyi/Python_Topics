c_ Solution o..
    # def sortColors(self, nums):
    #     """
    #     :type nums: List[int]
    #     :rtype: void Do not return anything, modify nums in-place instead.
    #     """
    #     # simple counting sort
    #     count = [0] * 3
    #     for num in nums:
    #         count[num] += 1
    #     pos = 0
    #     for index in range(3):
    #         while count[index] > 0:
    #             nums[pos] = index
    #             pos += 1
    #             count[index] -= 1
    #     return

    ___ sortColors  nums
        # https://leetcode.com/discuss/85658/sharing-c-solution-with-good-explanation
        low, mid, high = 0, 0, l.. nums) - 1
        w.. mid <= high:
            __ nums[mid] __ 0:
                # swap low mid
                nums[low], nums[mid] = nums[mid], nums[low]
                low += 1
                mid += 1
            ____ nums[mid] __ 1:
                mid += 1
            ____
                # swap mid high
                nums[high], nums[mid] = nums[mid], nums[high]
                high -= 1
        r_
