'''
Created on Mar 24, 2018

@author: tongq
'''
c_ Solution(o..
    ___ dominantIndex  nums
        """
        :type nums: List[int]
        :rtype: int
        """
        __ n.. nums:
            r.. -1
        first, fInd = f__('-inf'), -1
        second = f__('-inf')
        ___ i, num __ e..(nums
            __ num > first:
                second = first
                first = num
                fInd = i
            ____ num > second:
                second = num
        r.. fInd __ first >_ 2*second ____ -1
    
    ___ test
        testCases = [
            [3, 6, 1, 0],
            [1, 2, 3, 4],
        ]
        ___ nums __ testCases:
            print('nums: %s' % nums)
            result = dominantIndex(nums)
            print('result: %s' % result)
            print('-='*30+'-')

__ _____ __ _____
    Solution().test()
