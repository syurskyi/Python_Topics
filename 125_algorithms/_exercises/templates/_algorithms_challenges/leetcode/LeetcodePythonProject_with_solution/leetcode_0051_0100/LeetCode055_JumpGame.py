'''
Created on Jan 21, 2017

@author: MT
'''

c_ Solution(object):
    ___ canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        furthest = 0
        ___ i, num __ e..(nums):
            __ furthest >= i:
                furthest = max(furthest, i+num)
            __ furthest >= l..(nums)-1:
                r.. T..
        r.. F..
    
    ___ test
        testCases = [
            [2,3,1,1,4],
            [3,2,1,0,4],
        ]
        ___ nums __ testCases:
            print('nums: %s' % (nums))
            result = canJump(nums)
            print('result: %s' % (result))
            print('-='*15+'-')

__ __name__ __ '__main__':
    Solution().test()
