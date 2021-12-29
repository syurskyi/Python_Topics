'''
Created on Sep 4, 2017

@author: MT
'''
class Solution(object):
    ___ findUnsortedSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        numsSorted = s..(nums)
        i, j = 0, l..(nums)-1
        w.... i < j a.. numsSorted[i] __ nums[i]:
            i += 1
        __ i __ j:
            r.. 0
        w.... i < j a.. numsSorted[j] __ nums[j]:
            j -= 1
        r.. j-i+1
    
    ___ test(self):
        testCases = [
            [2, 6, 4, 8, 10, 9, 15],
            [1, 2, 3, 5],
        ]
        ___ nums __ testCases:
            print('nums: %s' % nums)
            result = self.findUnsortedSubarray(nums)
            print('result: %s' % result)
            print('-='*30+'-')

__ __name__ __ '__main__':
    Solution().test()
