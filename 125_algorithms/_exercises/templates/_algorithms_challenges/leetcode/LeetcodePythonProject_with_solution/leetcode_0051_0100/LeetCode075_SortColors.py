'''
Created on Jan 23, 2017

@author: MT
'''

c_ Solution(o..):
    ___ sortColors  nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        colors = [0]*3
        ___ num __ nums:
            colors[num]+=1
        i, j = 0, 0
        w.... j < 3:
            __ colors[j]:
                nums[i]=j
                colors[j] -= 1
                i += 1
            ____:
                j += 1
    
    ___ test
        testCases = [
            [2, 1, 0, 0, 1, 2, 2, 1],
        ]
        ___ nums __ testCases:
            print('nums: %s' % (nums))
            sortColors(nums)
            print('After sort')
            print('nums: %s' % (nums))
            print('-='*15+'-')
__ _____ __ _____
    Solution().test()
