'''
Created on Sep 5, 2017

@author: MT
'''
c_ Solution(o..
    ___ findLHS  nums
        """
        :type nums: List[int]
        :rtype: int
        """
        hashmap    # dict
        ___ num __ nums:
            hashmap[num] = hashmap.g.. num, 0)+1
        maxLen = 0
        ___ num, count __ hashmap.i..:
            __ num+1 __ hashmap:
                maxLen = m..(maxLen, count+hashmap[num+1])
        r.. maxLen
    
    ___ test
        testCases = [
            [1,3,2,2,5,2,3,7],
        ]
        ___ nums __ testCases:
            print('nums: %s' % nums)
            result = findLHS(nums)
            print('result: %s' % result)
            print('-='*30+'-')

__ _____ __ _____
    Solution().test()
