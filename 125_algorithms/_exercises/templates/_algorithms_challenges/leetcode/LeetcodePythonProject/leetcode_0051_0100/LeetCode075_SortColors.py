'''
Created on Jan 23, 2017

@author: MT
'''

class Solution(object
    ___ sortColors(self, nums
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        colors = [0]*3
        ___ num in nums:
            colors[num]+=1
        i, j = 0, 0
        w___ j < 3:
            __ colors[j]:
                nums[i]=j
                colors[j] -= 1
                i += 1
            ____
                j += 1
    
    ___ test(self
        testCases = [
            [2, 1, 0, 0, 1, 2, 2, 1],
        ]
        ___ nums in testCases:
            print('nums: %s' % (nums))
            self.sortColors(nums)
            print('After sort')
            print('nums: %s' % (nums))
            print('-='*15+'-')
__ __name__ __ '__main__':
    Solution().test()
