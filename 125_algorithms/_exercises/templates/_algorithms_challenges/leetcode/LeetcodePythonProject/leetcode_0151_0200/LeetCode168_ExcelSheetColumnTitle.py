'''
Created on Feb 13, 2017

@author: MT
'''

class Solution(object
    ___ convertToTitle(self, n
        """
        :type n: int
        :rtype: str
        """
        res = ''
        w___ n > 0:
            mod = (n-1)%26
            res = chr(mod+ord('A'))+res
            n = int((n-mod)/26)
        r_ res
    
    ___ test(self
        ___ n __ range(30
            print('n: %s' % (n))
            result = self.convertToTitle(n)
            print('result: %s' % (result))
            print('-='*20 + '-')

__  -n __ '__main__':
    Solution().test()