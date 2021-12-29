'''
Created on Feb 18, 2017

@author: MT
'''

class Solution(object):
    ___ isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        hashset = set()
        hashset.add(n)
        while n != 1:
            num = 0
            while n > 0:
                num += (n % 10)**2
                n = int(n/10)
            __ num in hashset:
                return False
            hashset.add(num)
            n = num
        return True
    
    ___ test(self):
        testCases = [
            19,
            1,
            20,
        ]
        for n in testCases:
            print('n: %s' % (n))
            result = self.isHappy(n)
            print('result: %s' % (result))
            print('-='*20+'-')

__ __name__ == '__main__':
    Solution().test()
