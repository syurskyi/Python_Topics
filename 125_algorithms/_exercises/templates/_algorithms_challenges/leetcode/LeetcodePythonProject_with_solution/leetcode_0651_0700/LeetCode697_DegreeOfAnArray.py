'''
Created on Oct 26, 2017

@author: MT
'''
c_ Solution(o..
    ___ findShortestSubArray  nums
        """
        :type nums: List[int]
        :rtype: int
        """
        __ n.. nums: r.. 0
        hashmap    # dict
        degree 0
        cands s..()
        ___ i, num __ e..(nums
            hashmap[num] hashmap.g.. num, [])+[i]
            __ l..(hashmap[num]) > degree:
                degree l..(hashmap[num])
                cands s..([num])
            ____ l..(hashmap[num]) __ degree:
                cands.add(num)
        minLen f__('inf')
        ___ num __ cands:
            __ l..(hashmap[num]) __ 1:
                r.. 1
            minLen m..(minLen, hashmap[num][-1]-hashmap[num][0]+1)
        r.. minLen
    
    ___ test
        testCases [
            [1, 2, 2, 3, 1],
            [1, 2, 2, 3, 1, 4, 2],
        ]
        ___ nums __ testCases:
            print('nums: %s' % nums)
            result findShortestSubArray(nums)
            print('result: %s' % result)
            print('-='*30+'-')

__ _____ __ _____
    Solution().test()
