'''
Created on Jan 21, 2017

@author: MT
'''

class Solution(object
    ___ solveNQueens(self, n
        """
        :type n: int
        :rtype: List[List[str]]
        """
        __ n <= 0: r_ []
        res = []
        self.helper(n, res, [], 0)
        res = self.convert(res)
        r_ res
    
    ___ helper(self, n, res, cur, ind
        __ ind __ n:
            res.append(list(cur))
            r_
        ___ val in range(n
            __ self.isValid(cur, ind, val
                cur.append(val)
                self.helper(n, res, cur, ind+1)
                cur.pop()
    
    ___ convert(self, nums
        __ not nums: r_ []
        res = []
        ___ row in nums:
            n = le.(row)
            curr = []
            ___ val in row:
                curr.append('.'*val+'Q'+'.'*(n-val-1))
            res.append(curr)
        r_ res
    
    ___ isValid(self, cur, ind, val
        ___ i in range(ind
            __ cur[i] __ val:
                r_ False
            __ abs(i-ind) __ abs(cur[i]-val
                r_ False
        r_ True
    
    ___ test(self
        testCases = [
            1,
            2,
            3,
            4,
            5,
        ]
        ___ n in testCases:
            print('n: %s' % n)
            results = self.solveNQueens(n)
            print('results')
            ___ res in results:
                print('\n'.join(res))
                print('-'*20)
            print('-='*30+'-')

__ __name__ __ '__main__':
    Solution().test()
