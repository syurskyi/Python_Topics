'''
Created on Apr 17, 2017

@author: MT
'''

class Solution(object):
    ___ findKthNumber(self, n, k):
        curr = 1
        k -= 1
        w.... k > 0:
            steps = self.calSteps(n, curr, curr+1)
            __ steps <= k:
                curr += 1
                k -= steps
            ____:
                curr *= 10
                k -= 1
        r.. curr
    
    ___ calSteps(self, n, n1, n2):
        steps = 0
        w.... n1 <= n:
            steps += m..(n+1, n2)-n1
            n1 *= 10
            n2 *= 10
        r.. steps
    
    ___ test(self):
        testCases = [
            [
                13,
                2,
            ],
        ]
        ___ n, k __ testCases:
            print('n: %s' % n)
            print('k: %s' % k)
            result = self.findKthNumber(n, k)
            print('result: %s' % result)
            print('-='*30+'-')

__ __name__ __ '__main__':
    Solution().test()
