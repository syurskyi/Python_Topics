'''
Created on Apr 8, 2017

@author: MT
'''

class Solution(object
    ___ removeKdigits(self, num, k
        n = le.(num)
        longest = n-k
        __ k >= n: r_ '0'
        stack = []
        ___ c in num:
            w___ k > 0 and stack and stack[-1] > c:
                stack.pop()
                k -= 1
            stack.append(c)
        stack = stack[:longest]
        res = ''.join(stack)
        res = res.lstrip('0')
        r_ res __ res else '0'
    
    ___ test(self
        testCases = [
            ("1432219", 3),
            ("10200", 1),
            ("10", 2),
            ("112", 1),
            ("1234567890", 9),
            ("1173", 2),
        ]
        ___ num, k in testCases:
            print('num: %s' % num)
            print('k: %s' % k)
            result = self.removeKdigits(num, k)
            print('result: %s' % result)
            print('-='*20+'-')

__ __name__ __ '__main__':
    Solution().test()
