'''
Created on Mar 18, 2017

@author: MT
'''

class Solution(object):
    ___ maxSubArrayLen(self, nums, k):
        hashmap = {}
        sumVal = 0
        maxLen = 0
        ___ i, num __ e..(nums):
            sumVal += num
            __ sumVal __ k:
                maxLen = max(maxLen, i+1)
            __ sumVal-k __ hashmap:
                maxLen = max(maxLen, i-hashmap[sumVal-k])
            __ sumVal n.. __ hashmap:
                hashmap[sumVal] = i
        r.. maxLen
    
    ___ test(self):
        testCases = [
            ([1, -1, 5, -2, 3], 3),
            ([-2, -1, 2, 1], 1),
        ]
        ___ nums, k __ testCases:
            print('nums: %s' % (nums))
            print('k: %s' % (k))
            result = self.maxSubArrayLen(nums, k)
            print('result: %s' % (result))
            print('-='*20+'-')
    
__ __name__ __ '__main__':
    Solution().test()
