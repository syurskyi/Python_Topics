'''
Created on May 10, 2017

@author: MT
'''

c_ Solution(o..
    ___ nextGreaterElement  findNums, nums
        """
        :type findNums: List[int]
        :type nums: List[int]
        :rtype: List[int]
        """
        res    # list
        ___ k, num0 __ e..(findNums
            ind = nums.i.. num0)
            ___ i __ r..(ind, l..(nums:
                __ nums[i] > num0:
                    res.a..(nums[i])
                    _____
            __ l..(res) __ k:
                res.a..(-1)
        r.. res
    
    ___ test
        testCases = [
            (
                [4, 1, 2],
                [1, 3, 4, 2],
            ),
        ]
        ___ findNums, nums __ testCases:
            result = nextGreaterElement(findNums, nums)
            print('result: %s' % result)
            print('-='*30+'-')

__ _____ __ _____
    Solution().test()
