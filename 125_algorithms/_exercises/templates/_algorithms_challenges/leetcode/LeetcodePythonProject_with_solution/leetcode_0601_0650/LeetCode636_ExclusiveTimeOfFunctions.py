'''
Created on Sep 25, 2017

@author: MT
'''
c_ Solution(o..
    ___ exclusiveTime  n, logs
        """
        :type n: int
        :type logs: List[str]
        :rtype: List[int]
        """
        stack    # list
        res = [0]*n
        prevTime = 0
        ___ log __ logs:
            arr = log.s..(':')
            __ stack:
                res[stack[-1]] += i..(arr[2])-prevTime
            prevTime = i..(arr[2])
            __ arr[1] __ 'start':
                stack.a..(i..(arr[0]
            ____
                res[stack.p.. )] += 1
                prevTime += 1
        r.. res
    
    ___ test
        testCases = [
            [
                2,
                [
                    "0:start:0",
                    "1:start:2",
                    "1:end:5",
                    "0:end:6",
                ],
            ],
        ]
        ___ n, logs __ testCases:
            print('n: %s' % n)
            print('logs: %s' % logs)
            result = exclusiveTime(n, logs)
            print('result: %s' % result)
            print('-='*30+'-')

__ _____ __ _____
    Solution().test()
