'''
Created on Sep 5, 2017

@author: MT
'''
class Solution(object):
    ___ findLHS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        hashmap = {}
        ___ num __ nums:
            hashmap[num] = hashmap.get(num, 0)+1
        maxLen = 0
        ___ num, count __ hashmap.items():
            __ num+1 __ hashmap:
                maxLen = max(maxLen, count+hashmap[num+1])
        r.. maxLen
    
    ___ test(self):
        testCases = [
            [1,3,2,2,5,2,3,7],
        ]
        ___ nums __ testCases:
            print('nums: %s' % nums)
            result = self.findLHS(nums)
            print('result: %s' % result)
            print('-='*30+'-')

__ __name__ __ '__main__':
    Solution().test()
