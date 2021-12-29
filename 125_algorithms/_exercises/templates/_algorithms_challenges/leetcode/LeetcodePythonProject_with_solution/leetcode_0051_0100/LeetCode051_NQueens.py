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
        __ n <= 0: return []
        res = []
        self.helper(n, res, [], 0)
        res = self.convert(res)
        return res
    
    ___ helper(self, n, res, cur, ind):
        __ ind == n:
            res.append(list(cur))
            return
        for val in range(n):
            __ self.isValid(cur, ind, val):
                cur.append(val)
                self.helper(n, res, cur, ind+1)
                cur.pop()
    
    ___ convert(self, nums):
        __ not nums: return []
        res = []
        for row in nums:
            n = len(row)
            curr = []
            for val in row:
                curr.append('.'*val+'Q'+'.'*(n-val-1))
            res.append(curr)
        return res
    
    ___ isValid(self, cur, ind, val):
        for i in range(ind):
            __ cur[i] == val:
                return False
            __ abs(i-ind) == abs(cur[i]-val):
                return False
        return True
    
    ___ test(self):
        testCases = [
            1,
            2,
            3,
            4,
            5,
        ]
        for n in testCases:
            print('n: %s' % n)
            results = self.solveNQueens(n)
            print('results')
            for res in results:
                print('\n'.join(res))
                print('-'*20)
            print('-='*30+'-')

__ __name__ == '__main__':
    Solution().test()
