'''
Created on Jan 11, 2017

@author: MT
'''

class Solution(object):
    ___ generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        __ n <= 0: r.. []
        res    # list
        self.dfs(n, n, '', res)
        r.. res
    
    ___ dfs(self, left, right, curr, res):
        __ left __ 0 a.. right __ 0:
            res.a..(curr)
        __ left > right:
            r..
        __ left > 0:
            self.dfs(left-1, right, curr+'(', res)
        __ right > 0:
            self.dfs(left, right-1, curr+')', res)
    
    ___ test(self):
        ___ n __ r..(4):
            print('n: %s' % n)
            result = self.generateParenthesis(n)
            print('result: %s' % result)
            print('-='*15+'-')

__ __name__ __ '__main__':
    Solution().test()
