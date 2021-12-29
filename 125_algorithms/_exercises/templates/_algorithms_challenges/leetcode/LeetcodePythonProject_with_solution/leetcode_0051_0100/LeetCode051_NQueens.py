'''
Created on Jan 21, 2017

@author: MT
'''

class Solution(object):
    ___ solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        __ n <= 0: r.. []
        res    # list
        self.helper(n, res, [], 0)
        res = self.convert(res)
        r.. res
    
    ___ helper(self, n, res, cur, ind):
        __ ind __ n:
            res.a..(l..(cur))
            r..
        ___ val __ r..(n):
            __ self.isValid(cur, ind, val):
                cur.a..(val)
                self.helper(n, res, cur, ind+1)
                cur.pop()
    
    ___ convert(self, nums):
        __ n.. nums: r.. []
        res    # list
        ___ row __ nums:
            n = l..(row)
            curr    # list
            ___ val __ row:
                curr.a..('.'*val+'Q'+'.'*(n-val-1))
            res.a..(curr)
        r.. res
    
    ___ isValid(self, cur, ind, val):
        ___ i __ r..(ind):
            __ cur[i] __ val:
                r.. False
            __ abs(i-ind) __ abs(cur[i]-val):
                r.. False
        r.. True
    
    ___ test(self):
        testCases = [
            1,
            2,
            3,
            4,
            5,
        ]
        ___ n __ testCases:
            print('n: %s' % n)
            results = self.solveNQueens(n)
            print('results')
            ___ res __ results:
                print('\n'.join(res))
                print('-'*20)
            print('-='*30+'-')

__ __name__ __ '__main__':
    Solution().test()
