'''
Created on Apr 17, 2017

@author: MT
'''

c_ Solution(object):
    ___ findDuplicates(self, nums):
        result    # list
        ___ num __ nums:
            ind = abs(num)-1
            __ nums[ind] < 0:
                result.a..(abs(num))
            ____:
                nums[ind] = -nums[ind]
        r.. result
    
    ___ test
        testCases = [
            [4,3,2,7,8,2,3,1],
            [10,2,5,10,9,1,1,4,3,7],
        ]
        ___ nums __ testCases:
            print('nums: %s' % nums)
            result = findDuplicates(nums)
            print('result: %s' % result)
            print('-='*20+'-')

__ __name__ __ '__main__':
    Solution().test()
