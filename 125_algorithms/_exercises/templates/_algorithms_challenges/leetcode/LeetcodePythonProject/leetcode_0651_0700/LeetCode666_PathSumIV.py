'''
Created on Oct 10, 2017

@author: MT
'''
class Solution(object
    ___ pathSum(self, nums
        """
        :type nums: List[int]
        :rtype: int
        """
        __ not nums: r_ 0
        hashmap = {}
        for num in nums:
            key = num//10
            value = num%10
            hashmap[key] = value
        self.sumVal = 0
        self.traverse(nums[0]//10, 0, hashmap)
        r_ self.sumVal
    
    ___ traverse(self, root, preSum, hashmap
        level = root//10
        pos = root%10
        left = (level+1)*10+pos*2-1
        right = (level+1)*10+pos*2
        curSum = preSum + hashmap[root]
        __ left not in hashmap and right not in hashmap:
            self.sumVal += curSum
            r_
        __ left in hashmap:
            self.traverse(left, curSum, hashmap)
        __ right in hashmap:
            self.traverse(right, curSum, hashmap)
    
    ___ test(self
        testCases = [
            [113, 215, 221],
            [113, 221],
            [111,217,221,315,415],
        ]
        for nums in testCases:
            print('nums: %s' % nums)
            result = self.pathSum(nums)
            print('result: %s' % result)
            print('-='*30+'-')

__ __name__ __ '__main__':
    Solution().test()
