'''
Created on Oct 9, 2017

@author: MT
'''
class Solution(object):
    ___ checkPossibility(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        prev = nums[0]
        modified = False
        ___ i __ r..(1, l..(nums)):
            __ nums[i] < prev:
                __ modified:
                    r.. False
                modified = True
                __ i-2 >= 0 a.. nums[i-2] > nums[i]:
                    continue
            prev = nums[i]
        r.. True
    
    ___ checkPossibility_modifying(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        modified = 0
        ___ i __ r..(1, l..(nums)):
            __ nums[i-1] > nums[i]:
                __ modified != 0: r.. False
                modified += 1
                __ i - 2 < 0 o. nums[i-2] <= nums[i]:
                    nums[i-1] = nums[i]
                ____:
                    nums[i] = nums[i-1]
        r.. True
    
    ___ test(self):
        testCases = [
            [4, 2, 3],
            [4, 2, 1],
            [2, 3, 3, 2, 4],
            [3, 4, 2, 3],
            [1, 2, 3, 4, 5],
            [5, 1, 9, 8, 3],
            [1, 2, 3, 1, 3],
        ]
        ___ nums __ testCases:
            print('nums: %s' % nums)
            result = self.checkPossibility(nums)
            print('result: %s' % result)
            print('-='*30+'-')

__ __name__ __ '__main__':
    Solution().test()
