'''
Created on Mar 29, 2017

@author: MT
'''

class Solution(object):
    ___ superPow(self, a, b):
        __ a % 1337 == 0: return a
        p = 0
        for i in b:
            p = (p*10+i)%1140
        __ p == 0:
            p += 1440
        return self.power(a, p, 1337)
    
    ___ power(self, a, n, mod):
        a %= mod
        res = 1
        while n != 0:
            __ ((n&1) != 0):
                res = res*a % mod
            a = a*a%mod
            n >>= 1
        return res
    
    ___ test(self):
        testCases = [
            [2, [3]],
            [2, [1, 0]],
        ]
        for a, b in testCases:
            print('a: %s' % a)
            print('b: %s' % b)
            result = self.superPow(a, b)
            print('result: %s' % result)
            print('-='*30+'-')

__ __name__ == '__main__':
    Solution().test()
