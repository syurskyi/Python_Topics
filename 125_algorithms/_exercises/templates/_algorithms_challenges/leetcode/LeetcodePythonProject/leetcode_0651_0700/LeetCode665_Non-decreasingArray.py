'''
Created on Oct 9, 2017

@author: MT
'''
class Solution(object
    ___ checkPossibility(self, nums
        """
        :type nums: List[int]
        :rtype: bool
        """
        prev = nums[0]
        modified = False
        ___ i in range(1, le.(nums)):
            __ nums[i] < prev:
                __ modified:
                    r_ False
                modified = True
                __ i-2 >= 0 and nums[i-2] > nums[i]:
                    continue
            prev = nums[i]
        r_ True
    
    ___ checkPossibility_modifying(self, nums
        """
        :type nums: List[int]
        :rtype: bool
        """
        modified = 0
        ___ i in range(1, le.(nums)):
            __ nums[i-1] > nums[i]:
                __ modified != 0: r_ False
                modified += 1
                __ i - 2 < 0 or nums[i-2] <= nums[i]:
                    nums[i-1] = nums[i]
                ____
                    nums[i] = nums[i-1]
        r_ True
    
    ___ test(self
        testCases = [
            [4, 2, 3],
            [4, 2, 1],
            [2, 3, 3, 2, 4],
            [3, 4, 2, 3],
            [1, 2, 3, 4, 5],
            [5, 1, 9, 8, 3],
            [1, 2, 3, 1, 3],
        ]
        ___ nums in testCases:
            print('nums: %s' % nums)
            result = self.checkPossibility(nums)
            print('result: %s' % result)
            print('-='*30+'-')

__ __name__ __ '__main__':
    Solution().test()
