'''
Created on Oct 15, 2017

@author: MT
'''
class Solution(object
    ___ findNumberOfLIS(self, nums
        """
        :type nums: List[int]
        :rtype: int
        """
        __ not nums: r_ 0
        n = le.(nums)
        res = 0
        maxLen = 0
        lengths = [0]*n
        counts = [0]*n
        ___ i in range(n
            lengths[i], counts[i] = 1, 1
            ___ j in range(i
                __ nums[i] > nums[j]:
                    __ lengths[i] __ lengths[j]+1:
                        counts[i] += counts[j]
                    ____ lengths[i] < lengths[j]+1:
                        lengths[i] = lengths[j] + 1
                        counts[i] = counts[j]
            __ maxLen __ lengths[i]:
                res += counts[i]
            ____ maxLen < lengths[i]:
                maxLen = lengths[i]
                res = counts[i]
        r_ res
    
    ___ test(self
        testCases = [
            [1, 3, 5, 4, 7],
            [2, 2, 2, 2, 2],
            [1, 2, 4, 3, 5, 4, 7, 2],
        ]
        ___ nums in testCases:
            print('nums: %s' % nums)
            result = self.findNumberOfLIS(nums)
            print('result: %s' % result)
            print('-='*30+'-')

__ __name__ __ '__main__':
    Solution().test()
