'''
Created on Jan 21, 2017

@author: MT
'''

class Solution(object
    ___ canJump(self, nums
        """
        :type nums: List[int]
        :rtype: bool
        """
        furthest = 0
        ___ i, num in enumerate(nums
            __ furthest >= i:
                furthest = max(furthest, i+num)
            __ furthest >= le.(nums)-1:
                r_ True
        r_ False
    
    ___ test(self
        testCases = [
            [2,3,1,1,4],
            [3,2,1,0,4],
        ]
        ___ nums in testCases:
            print('nums: %s' % (nums))
            result = self.canJump(nums)
            print('result: %s' % (result))
            print('-='*15+'-')

__ __name__ __ '__main__':
    Solution().test()
