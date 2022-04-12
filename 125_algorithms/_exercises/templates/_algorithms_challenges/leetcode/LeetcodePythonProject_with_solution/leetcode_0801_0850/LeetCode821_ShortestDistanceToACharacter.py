'''
Created on May 2, 2018

@author: tongq
'''
c_ Solution(o..
    ___ shortestToChar  S, C
        """
        :type S: str
        :type C: str
        :rtype: List[int]
        """
        s, c S, C
        arr    # list
        ___ i, c0 __ e..(s
            __ c0 __ c:
                arr.a..(i)
        res    # list
        j 0
        ___ i __ r..(l..(s:
            __ i < arr[j]:
                val arr[j]-i
                __ j > 0
                    val m..(val, i-arr[j-1])
            ____ i __ arr[j]:
                val 0
                __ j < l..(arr)-1:
                    j += 1
            ____
                val i-arr[j]
            res.a..(val)
        r.. res
    
    ___ test
        testCases [
            [
                'loveleetcode', 'e',
            ],
        ]
        ___ s, c __ testCases:
            print('s: %s' % s)
            print('c: %s' % c)
            result shortestToChar(s, c)
            print('result: %s' % result)
            print('-='*30+'-')

__ _____ __ _____
    Solution().test()
