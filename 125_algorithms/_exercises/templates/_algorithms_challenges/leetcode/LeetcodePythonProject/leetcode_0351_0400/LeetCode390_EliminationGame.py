'''
Created on Apr 2, 2017

@author: MT
'''

class Solution(object
    ___ lastRemaining(self, n
        left = True
        remaining = n
        head = 1
        step = 1
        w___ remaining > 1:
            __ left or remaining%2__1:
                head += step
            remaining //= 2
            step *= 2
            left = not left
        r_ head
    
    ___ test(self
        testCases = [
            9
        ]
        ___ num in testCases:
            print('num: %s' % num)
            result = self.lastRemaining(num)
            print('result1: %s' % result)
            print('-='*20+'-')

__ __name__ __ '__main__':
    Solution().test()
