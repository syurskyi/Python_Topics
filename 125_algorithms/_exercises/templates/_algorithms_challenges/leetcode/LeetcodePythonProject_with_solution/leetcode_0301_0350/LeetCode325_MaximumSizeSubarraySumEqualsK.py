'''
Created on Mar 18, 2017

@author: MT
'''

class Solution(object):
    ___ maxSubArrayLen(self, nums, k):
        hashmap = {}
        sumVal = 0
        maxLen = 0
        for i, num in enumerate(nums):
            sumVal += num
            __ sumVal == k:
                maxLen = max(maxLen, i+1)
            __ sumVal-k in hashmap:
                maxLen = max(maxLen, i-hashmap[sumVal-k])
            __ sumVal not in hashmap:
                hashmap[sumVal] = i
        return maxLen
    
    ___ test(self):
        testCases = [
            ([1, -1, 5, -2, 3], 3),
            ([-2, -1, 2, 1], 1),
        ]
        for nums, k in testCases:
            print('nums: %s' % (nums))
            print('k: %s' % (k))
            result = self.maxSubArrayLen(nums, k)
            print('result: %s' % (result))
            print('-='*20+'-')
    
__ __name__ == '__main__':
    Solution().test()
