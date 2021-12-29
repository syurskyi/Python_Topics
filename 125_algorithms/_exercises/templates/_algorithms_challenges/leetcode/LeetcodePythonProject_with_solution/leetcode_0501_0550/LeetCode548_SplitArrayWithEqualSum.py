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
        __ n.. nums: r.. False
        sumVals = [nums[0]]
        n = l..(nums)
        ___ i __ r..(1, n):
            sumVals.a..(sumVals[-1]+nums[i])
        ___ j __ r..(3, n-3):
            hashset = set()
            ___ i __ r..(1, j-1):
                __ sumVals[i-1] __ sumVals[j-1]-sumVals[i]:
                    hashset.add(sumVals[i-1])
            ___ k __ r..(j+2, n-1):
                __ sumVals[n-1]-sumVals[k] __ sumVals[k-1]-sumVals[j] and\
                    sumVals[k-1]-sumVals[j] __ hashset:
                    r.. True
        r.. False
    
    ___ test(self):
        testCases = [
            [1,2,1,2,1,2,1],
        ]
        ___ nums __ testCases:
            print('nums: %s' % nums)
            result = self.splitArray(nums)
            print('result: %s' % result)
            print('-='*30+'-')

__ __name__ __ '__main__':
    Solution().test()
