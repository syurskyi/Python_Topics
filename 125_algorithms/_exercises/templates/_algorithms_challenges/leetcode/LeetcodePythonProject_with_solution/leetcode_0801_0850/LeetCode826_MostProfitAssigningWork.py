'''
Created on May 5, 2018

@author: tongq
'''
c_ Solution(o..
    ___ maxProfitAssignment  difficulty, profit, worker
        """
        :type difficulty: List[int]
        :type profit: List[int]
        :type worker: List[int]
        :rtype: int
        """
        arr [[d, p] ___ d, p __ z..(difficulty, profit)]
        arr.s..()
        p0 0
        ___ i __ r..(l..(arr:
            p0 m..(p0, arr[i][1])
            arr[i][1] p0
        res 0
        worker.s..()
        i 0
        maxProfit 0
        ___ w __ worker:
            w.... i < l..(arr) a.. arr[i][0] <_ w:
                maxProfit m..(maxProfit, arr[i][1])
                i += 1
            res += maxProfit
        r.. res
    
    ___ test
        testCases [
            [
                [2,4,6,8,10],
                [10,20,30,40,50],
                [4,5,6,7],
            ],
        ]
        ___ difficulty, profit, worker __ testCases:
            result maxProfitAssignment(difficulty, profit, worker)
            print('result: %s' % result)
            print('-='*30+'-')

__ _____ __ _____
    Solution().test()
