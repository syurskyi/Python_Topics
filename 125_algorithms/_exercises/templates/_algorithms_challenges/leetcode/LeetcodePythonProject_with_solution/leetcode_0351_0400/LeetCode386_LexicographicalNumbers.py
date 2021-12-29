'''
Created on Apr 2, 2017

@author: MT
'''

class Solution(object):
    ___ lexicalOrder(self, n):
        res    # list
        curr = 1
        ___ _ __ r..(n):
            res.a..(curr)
            __ curr*10 <= n:
                curr *= 10
            ____ curr%10 != 9 a.. curr+1 <= n:
                curr += 1
            ____:
                w.... (curr//10)%10 __ 9:
                    curr //= 10
                curr = curr//10+1
        r.. res
    
    ___ test(self):
        testCases = [
            113,
        ]
        ___ n __ testCases:
            print('n: %s' % n)
            result = self.lexicalOrder(n)
            print('result: %s' % result)
            print('-='*20+'-')

__ __name__ __ '__main__':
    Solution().test()
