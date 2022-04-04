'''
Created on Feb 9, 2017

@author: MT
'''

c_ Solution(o..
    ___ candy  ratings
        """
        :type ratings: List[int]
        :rtype: int
        """
        n = l..(ratings)
        left = [0]*n
        left[0] = 1
        ___ i __ r..(1, n
            __ ratings[i] > ratings[i-1]:
                left[i] = left[i-1]+1
            ____
                left[i] = 1
        right = [0]*n
        right[-1] = 1
        ___ i __ r..(n-2, -1, -1
            __ ratings[i] > ratings[i+1]:
                right[i] = right[i+1]+1
            ____
                right[i] = 1
        res = 0
        ___ i __ r..(n
            res += m..(left[i], right[i])
        r.. res
    
    ___ test
        testCases = [
            [1, 0, 2],
            [1, 2, 2],
            [1,3,2,2,1],
            [1, 2, 3, 1, 3, 3, 2],
        ]
        ___ ratings __ testCases:
            print('ratings: %s' % (ratings
            result = candy(ratings)
            print('result: %s' % (result
            print('-='*20+'-')

__ _____ __ _____
    Solution().test()