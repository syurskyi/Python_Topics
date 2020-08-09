'''
Created on Feb 18, 2017

@author: MT
'''

class Solution(object
    ___ isHappy(self, n
        """
        :type n: int
        :rtype: bool
        """
        hashset = set()
        hashset.add(n)
        w___ n != 1:
            num = 0
            w___ n > 0:
                num += (n % 10)**2
                n = int(n/10)
            __ num in hashset:
                r_ False
            hashset.add(num)
            n = num
        r_ True
    
    ___ test(self
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

__ __name__ __ '__main__':
    Solution().test()
