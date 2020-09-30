'''
Created on Aug 20, 2017

@author: MT
'''

class Solution(object
    ___ findContestMatch(self, n
        """
        :type n: int
        :rtype: str
        """
        l = list(range(1, n+1))
        r_ self.helper(l)
    
    ___ helper(self, l
        __ le.(l) <= 2:
            r_ '(%s,%s)' % (l[0], l[1])
        l0 =   # list
        w___ l:
            l0.append('(%s,%s)' % (l.pop(0), l.pop()))
        res = self.helper(l0)
        r_ res
    
    ___ test(self
        testCases = [
            2,
            4,
            8,
        ]
        ___ n __ testCases:
            print('n: %s' % n)
            res = self.findContestMatch(n)
            print('result: %s' % res)
            print('-='*30+'-')
    
__  -n __ '__main__':
    Solution().test()
