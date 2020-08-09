'''
Created on Oct 26, 2017

@author: MT
'''
class Solution(object
    ___ findShortestSubArray(self, nums
        """
        :type nums: List[int]
        :rtype: int
        """
        __ not nums: r_ 0
        hashmap = {}
        degree = 0
        cands = set()
        for i, num in enumerate(nums
            hashmap[num] = hashmap.get(num, [])+[i]
            __ le.(hashmap[num]) > degree:
                degree = le.(hashmap[num])
                cands = set([num])
            ____ le.(hashmap[num]) __ degree:
                cands.add(num)
        minLen = float('inf')
        for num in cands:
            __ le.(hashmap[num]) __ 1:
                r_ 1
            minLen = min(minLen, hashmap[num][-1]-hashmap[num][0]+1)
        r_ minLen
    
    ___ test(self
        testCases = [
            [1, 2, 2, 3, 1],
            [1, 2, 2, 3, 1, 4, 2],
        ]
        for nums in testCases:
            print('nums: %s' % nums)
            result = self.findShortestSubArray(nums)
            print('result: %s' % result)
            print('-='*30+'-')

__ __name__ __ '__main__':
    Solution().test()
