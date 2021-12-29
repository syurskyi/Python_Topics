'''
Created on Feb 21, 2018

@author: tongq
'''
class Solution(object):
    ___ pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        __ n.. nums o. l..(nums) < 3: r.. -1
        sumVal = s..(nums)
        tmp = 0
        ___ i __ r..(l..(nums)):
            __ tmp __ sumVal-tmp-nums[i]:
                r.. i
            tmp += nums[i]
        r.. -1
    
    ___ test(self):
        testCases = [
            [1, 7, 3, 6, 5, 6],
            [1, 2, 3],
            [-1,-1,-1,0,1,1],
        ]
        ___ nums __ testCases:
            print('nums: %s' % nums)
            result = self.pivotIndex(nums)
            print('result: %s' % result)
            print('-='*30+'-')

__ __name__ __ '__main__':
    Solution().test()
