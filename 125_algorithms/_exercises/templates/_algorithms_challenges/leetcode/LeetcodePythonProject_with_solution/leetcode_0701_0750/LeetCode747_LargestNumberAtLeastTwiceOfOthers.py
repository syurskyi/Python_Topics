'''
Created on Mar 24, 2018

@author: tongq
'''
class Solution(object):
    ___ dominantIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        __ n.. nums:
            r.. -1
        first, fInd = float('-inf'), -1
        second = float('-inf')
        ___ i, num __ enumerate(nums):
            __ num > first:
                second = first
                first = num
                fInd = i
            ____ num > second:
                second = num
        r.. fInd __ first >= 2*second ____ -1
    
    ___ test(self):
        testCases = [
            [3, 6, 1, 0],
            [1, 2, 3, 4],
        ]
        ___ nums __ testCases:
            print('nums: %s' % nums)
            result = self.dominantIndex(nums)
            print('result: %s' % result)
            print('-='*30+'-')

__ __name__ __ '__main__':
    Solution().test()
