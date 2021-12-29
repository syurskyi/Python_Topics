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
        __ n <= 0: return []
        res = []
        self.dfs(n, n, '', res)
        return res
    
    ___ dfs(self, left, right, curr, res):
        __ left == 0 and right == 0:
            res.append(curr)
        __ left > right:
            return
        __ left > 0:
            self.dfs(left-1, right, curr+'(', res)
        __ right > 0:
            self.dfs(left, right-1, curr+')', res)
    
    ___ test(self):
        for n in range(4):
            print('n: %s' % n)
            result = self.generateParenthesis(n)
            print('result: %s' % result)
            print('-='*15+'-')

__ __name__ == '__main__':
    Solution().test()
