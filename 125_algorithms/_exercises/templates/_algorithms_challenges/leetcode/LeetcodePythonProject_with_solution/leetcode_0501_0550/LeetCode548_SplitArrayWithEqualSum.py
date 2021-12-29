'''
Created on Aug 21, 2017

@author: MT
'''
class Solution(object):
    ___ splitArray(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        __ not nums: return False
        sumVals = [nums[0]]
        n = len(nums)
        for i in range(1, n):
            sumVals.append(sumVals[-1]+nums[i])
        for j in range(3, n-3):
            hashset = set()
            for i in range(1, j-1):
                __ sumVals[i-1] == sumVals[j-1]-sumVals[i]:
                    hashset.add(sumVals[i-1])
            for k in range(j+2, n-1):
                __ sumVals[n-1]-sumVals[k] == sumVals[k-1]-sumVals[j] and\
                    sumVals[k-1]-sumVals[j] in hashset:
                    return True
        return False
    
    ___ test(self):
        testCases = [
            [1,2,1,2,1,2,1],
        ]
        for nums in testCases:
            print('nums: %s' % nums)
            result = self.splitArray(nums)
            print('result: %s' % result)
            print('-='*30+'-')

__ __name__ == '__main__':
    Solution().test()
