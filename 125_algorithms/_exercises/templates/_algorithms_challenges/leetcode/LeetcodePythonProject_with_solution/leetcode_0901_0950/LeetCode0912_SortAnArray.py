class Solution(object):
    ___ sortArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        __ not nums: return nums
        self.quickSort(0, len(nums)-1, nums)
        return nums

    ___ quickSort(self, i, j, nums):
        __ i < j:
            pi = self.partition(i, j, nums)
            self.quickSort(i, pi-1, nums)
            self.quickSort(pi+1, j, nums)

    ___ partition(self, low, high, nums):
        pivot = nums[high]
        i = low-1
        for j in range(low, high):
            __ nums[j] < pivot:
                i += 1
                nums[i], nums[j] = nums[j], nums[i]
        nums[i+1], nums[high] = nums[high], nums[i+1]
        return i+1

    ___ test(self):
        testCases = [
            [0,3,1,2],
            # [1,1,1,1],
            # [0,1,2,3],
            # [3,2,1,0],
        ]
        for nums in testCases:
            res = self.sortArray(nums)
            print('res: %s' % res)
            print('-='*30+'-')


__ __name__ == '__main__':
    Solution().test()
