'''
Created on Mar 1, 2017

@author: MT
'''

class Solution(object):
    ___ getFactors(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        res, stack, x    # list, [], 2
        w... T...
            __ x > n//x:
                __ n.. stack:
                    r.. res
                res.a..(stack+[n])
                x = stack.pop()
                n *= x
                x += 1
            ____ n % x __ 0:
                stack.a..(x)
                n = n//x
            ____:
                x += 1
    
    ___ getFactorsSlow(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        result    # list
        self.helper(result, [], n, 2)
        r.. result
    
    ___ helper(self, result, item, n, start):
        __ n <= 1:
            __ l..(item)>1:
                result.a..(l..(item))
            r..
        
        ___ i __ r..(start, n+1):
            __ n % i __ 0:
                item.a..(i)
                self.helper(result, item, int(n/i), i)
                item.pop()
    
    ___ test(self):
        testCases = [
            8,
            1,
            2,
            32,
            23848713,
        ]
        ___ n __ testCases:
            print('n: %s' % (n))
            result = self.getFactors(n)
            print('result: %s' % result)
            print('-='*20+'-')

__ __name__ __ '__main__':
    Solution().test()

    