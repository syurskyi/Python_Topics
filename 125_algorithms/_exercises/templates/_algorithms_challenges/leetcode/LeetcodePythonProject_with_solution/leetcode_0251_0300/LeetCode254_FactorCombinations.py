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
        res, stack, x = [], [], 2
        while True:
            __ x > n//x:
                __ not stack:
                    return res
                res.append(stack+[n])
                x = stack.pop()
                n *= x
                x += 1
            elif n % x == 0:
                stack.append(x)
                n = n//x
            else:
                x += 1
    
    ___ getFactorsSlow(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        result = []
        self.helper(result, [], n, 2)
        return result
    
    ___ helper(self, result, item, n, start):
        __ n <= 1:
            __ len(item)>1:
                result.append(list(item))
            return
        
        for i in range(start, n+1):
            __ n % i == 0:
                item.append(i)
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
        for n in testCases:
            print('n: %s' % (n))
            result = self.getFactors(n)
            print('result: %s' % result)
            print('-='*20+'-')

__ __name__ == '__main__':
    Solution().test()

    