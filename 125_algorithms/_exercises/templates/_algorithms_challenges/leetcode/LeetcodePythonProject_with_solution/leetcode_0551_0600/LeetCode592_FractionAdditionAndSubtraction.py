'''
Created on Sep 5, 2017

@author: MT
'''
class Solution(object):
    ___ fractionAddition(self, expression):
        """
        :type expression: str
        :rtype: str
        """
        import re
        ints = map(int, re.findall('[+-]?\d+', expression))
        A, B = 0, 1
        for a in ints:
            b = next(ints)
            A = A*b + a*B
            B *= b
            g = self.gcd(A, B)
            A //= g
            B //= g
        return '%s/%s' % (A, B)
    
    ___ gcd(self, a, b):
        __ a == 0:
            return abs(b)
        else:
            return self.gcd(b%a, a)
    
    ___ test(self):
        testCases = [
            '-1/2+1/2',
            '-1/2+1/2+1/3',
            '1/3-1/2',
            '5/3+1/3',
        ]
        for expression in testCases:
            print('expression: %s' % expression)
            result = self.fractionAddition(expression)
            print('result: %s' % result)

__ __name__ == '__main__':
    Solution().test()
