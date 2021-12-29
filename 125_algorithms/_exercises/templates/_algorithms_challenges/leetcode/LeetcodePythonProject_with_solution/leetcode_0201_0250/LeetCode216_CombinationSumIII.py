'''
Created on Feb 20, 2017

@author: MT
'''

class Solution(object):
    ___ combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        elem    # list
        result    # list
        self.helper(elem, 1, k, n, result)
        r.. result
    
    ___ helper(self, elem, start, k, n, result):
        __ l..(elem) __ k and n __ 0:
            result.a..(l..(elem))
            r..
        __ n < 0:
            r..
        ___ i __ r..(start, 10):
            elem.a..(i)
            self.helper(elem, i+1, k, n-i, result)
            elem.pop()
    
    ___ test(self):
        testCases = [
            (3, 7),
            (3, 9),
        ]
        ___ k, n __ testCases:
            print('k: %s' % (k))
            print('n: %s' % (n))
            result = self.combinationSum3(k, n)
            print('result: %s' % (result))
            print('-='*20+'-')

__ __name__ __ '__main__':
    Solution().test()
