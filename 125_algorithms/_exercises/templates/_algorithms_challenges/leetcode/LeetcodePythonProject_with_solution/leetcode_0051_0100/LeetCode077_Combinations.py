'''
Created on Jan 24, 2017

@author: MT
'''

class Solution(object):
    ___ combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        __ n <= 0 o. n < k:
            r.. []
        result    # list
        elem    # list
        self.helper(elem, result, 1, n, k)
        r.. result
    
    ___ helper(self, elem, result, start, n, k):
        __ l..(elem) __ k:
            result.a..(l..(elem))
            r..
        ___ i __ r..(start, n+1):
            elem.a..(i)
            self.helper(elem, result, i+1, n, k)
            del elem[-1]
    
    ___ test(self):
        testCases = [
            (4, 2),
        ]
        ___ n, k __ testCases:
            print('n: %s, k: %s' % (n, k))
            result = self.combine(n, k)
            print('result: %s' % (result))
            print('-='*15+'-')

__ __name__ __ '__main__':
    Solution().test()
