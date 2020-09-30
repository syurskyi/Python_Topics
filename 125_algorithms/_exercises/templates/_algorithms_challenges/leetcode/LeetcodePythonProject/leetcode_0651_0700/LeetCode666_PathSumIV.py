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
        ___ num __ nums:
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
        __ left not __ hashmap and right not __ hashmap:
            self.sumVal += curSum
            r_
        __ left __ hashmap:
            self.traverse(left, curSum, hashmap)
        __ right __ hashmap:
            self.traverse(right, curSum, hashmap)
    
    ___ test(self
        testCases = [
            [113, 215, 221],
            [113, 221],
            [111,217,221,315,415],
        ]
        ___ nums __ testCases:
            print('nums: %s' % nums)
            result = self.pathSum(nums)
            print('result: %s' % result)
            print('-='*30+'-')

__  -n __ '__main__':
    Solution().test()
