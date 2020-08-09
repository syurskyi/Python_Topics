'''
Created on Apr 2, 2017

@author: MT
'''

class Solution(object
    ___ lexicalOrder(self, n
        res = []
        curr = 1
        ___ _ in range(n
            res.append(curr)
            __ curr*10 <= n:
                curr *= 10
            ____ curr%10 != 9 and curr+1 <= n:
                curr += 1
            ____
                w___ (curr//10)%10 __ 9:
                    curr //= 10
                curr = curr//10+1
        r_ res
    
    ___ test(self
        testCases = [
            113,
        ]
        ___ n in testCases:
            print('n: %s' % n)
            result = self.lexicalOrder(n)
            print('result: %s' % result)
            print('-='*20+'-')

__ __name__ __ '__main__':
    Solution().test()
