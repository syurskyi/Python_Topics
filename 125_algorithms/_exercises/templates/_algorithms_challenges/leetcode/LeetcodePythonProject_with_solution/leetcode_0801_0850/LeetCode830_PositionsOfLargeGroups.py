'''
Created on May 6, 2018

@author: tongq
'''
c_ Solution(o..
    ___ largeGroupPositions  S
        """
        :type S: str
        :rtype: List[List[int]]
        """
        s S
        res    # list
        left 0
        ___ i __ r..(l..(s)+1
            __ i __ l..(s) o. s[i] !_ s[left]:
                __ i-left >_ 3:
                    res.a..([left, i-1])
                left i
        r.. res
    
    ___ test
        testCases [
            'aaa',
            'abbxxxxzzy',
            'abc',
            'abcdddeeeeaabbbcd',
        ]
        ___ s __ testCases:
            result largeGroupPositions(s)
            print('result: %s' % result)
            print('-='*30+'-')

__ _____ __ _____
    Solution().test()
