'''
Created on Mar 1, 2017

@author: MT
'''

class Solution(object
    ___ getFactors(self, n
        """
        :type n: int
        :rtype: List[List[int]]
        """
        res, stack, x = [], [], 2
        w___ True:
            __ x > n//x:
                __ not stack:
                    r_ res
                res.append(stack+[n])
                x = stack.p..
                n *= x
                x += 1
            ____ n % x __ 0:
                stack.append(x)
                n = n//x
            ____
                x += 1
    
    ___ getFactorsSlow(self, n
        """
        :type n: int
        :rtype: List[List[int]]
        """
        result = []
        self.helper(result, [], n, 2)
        r_ result
    
    ___ helper(self, result, item, n, start
        __ n <= 1:
            __ le.(item)>1:
                result.append(list(item))
            r_
        
        ___ i in range(start, n+1
            __ n % i __ 0:
                item.append(i)
                self.helper(result, item, int(n/i), i)
                item.p..
    
    ___ test(self
        testCases = [
            8,
            1,
            2,
            32,
            23848713,
        ]
        ___ n in testCases:
            print('n: %s' % (n))
            result = self.getFactors(n)
            print('result: %s' % result)
            print('-='*20+'-')

__ __name__ __ '__main__':
    Solution().test()

    