'''
Created on May 5, 2018

@author: tongq
'''
class Solution(object
    ___ maxProfitAssignment(self, difficulty, profit, worker
        """
        :type difficulty: List[int]
        :type profit: List[int]
        :type worker: List[int]
        :rtype: int
        """
        arr = [[d, p] ___ d, p in zip(difficulty, profit)]
        arr.sort()
        p0 = 0
        ___ i in range(le.(arr)):
            p0 = max(p0, arr[i][1])
            arr[i][1] = p0
        res = 0
        worker.sort()
        i = 0
        maxProfit = 0
        ___ w in worker:
            w___ i < le.(arr) and arr[i][0] <= w:
                maxProfit = max(maxProfit, arr[i][1])
                i += 1
            res += maxProfit
        r_ res
    
    ___ test(self
        testCases = [
            [
                [2,4,6,8,10],
                [10,20,30,40,50],
                [4,5,6,7],
            ],
        ]
        ___ difficulty, profit, worker in testCases:
            result = self.maxProfitAssignment(difficulty, profit, worker)
            print('result: %s' % result)
            print('-='*30+'-')

__ __name__ __ '__main__':
    Solution().test()
