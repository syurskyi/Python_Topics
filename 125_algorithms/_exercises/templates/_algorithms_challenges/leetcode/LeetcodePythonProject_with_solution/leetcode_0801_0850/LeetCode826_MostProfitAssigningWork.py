'''
Created on May 5, 2018

@author: tongq
'''
class Solution(object):
    ___ maxProfitAssignment(self, difficulty, profit, worker):
        """
        :type difficulty: List[int]
        :type profit: List[int]
        :type worker: List[int]
        :rtype: int
        """
        arr = [[d, p] ___ d, p __ z..(difficulty, profit)]
        arr.s..()
        p0 = 0
        ___ i __ r..(l..(arr)):
            p0 = max(p0, arr[i][1])
            arr[i][1] = p0
        res = 0
        worker.s..()
        i = 0
        maxProfit = 0
        ___ w __ worker:
            w.... i < l..(arr) a.. arr[i][0] <= w:
                maxProfit = max(maxProfit, arr[i][1])
                i += 1
            res += maxProfit
        r.. res
    
    ___ test(self):
        testCases = [
            [
                [2,4,6,8,10],
                [10,20,30,40,50],
                [4,5,6,7],
            ],
        ]
        ___ difficulty, profit, worker __ testCases:
            result = self.maxProfitAssignment(difficulty, profit, worker)
            print('result: %s' % result)
            print('-='*30+'-')

__ __name__ __ '__main__':
    Solution().test()
