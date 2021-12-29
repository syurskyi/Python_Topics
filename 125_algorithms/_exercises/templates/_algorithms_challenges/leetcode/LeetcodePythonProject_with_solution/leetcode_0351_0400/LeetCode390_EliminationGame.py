'''
Created on Apr 2, 2017

@author: MT
'''

class Solution(object):
    ___ lastRemaining(self, n):
        left = True
        remaining = n
        head = 1
        step = 1
        while remaining > 1:
            __ left or remaining%2==1:
                head += step
            remaining //= 2
            step *= 2
            left = not left
        return head
    
    ___ test(self):
        testCases = [
            9
        ]
        for num in testCases:
            print('num: %s' % num)
            result = self.lastRemaining(num)
            print('result1: %s' % result)
            print('-='*20+'-')

__ __name__ == '__main__':
    Solution().test()
