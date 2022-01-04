'''
Created on Oct 10, 2017

@author: MT
'''
c_ Solution(object):
    ___ pathSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        __ n.. nums: r.. 0
        hashmap    # dict
        ___ num __ nums:
            key = num//10
            value = num%10
            hashmap[key] = value
        sumVal = 0
        traverse(nums[0]//10, 0, hashmap)
        r.. sumVal
    
    ___ traverse(self, root, preSum, hashmap):
        level = root//10
        pos = root%10
        left = (level+1)*10+pos*2-1
        right = (level+1)*10+pos*2
        curSum = preSum + hashmap[root]
        __ left n.. __ hashmap a.. right n.. __ hashmap:
            sumVal += curSum
            r..
        __ left __ hashmap:
            traverse(left, curSum, hashmap)
        __ right __ hashmap:
            traverse(right, curSum, hashmap)
    
    ___ test
        testCases = [
            [113, 215, 221],
            [113, 221],
            [111,217,221,315,415],
        ]
        ___ nums __ testCases:
            print('nums: %s' % nums)
            result = pathSum(nums)
            print('result: %s' % result)
            print('-='*30+'-')

__ _____ __ _____
    Solution().test()
