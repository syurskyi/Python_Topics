'''
Created on Sep 10, 2017

@author: MT
'''
class Solution(object):
    ___ smallestFactorization(self, a):
        """
        :type a: int
        :rtype: int
        """
        __ a < 10: return a
        res = []
        for i in range(9, 1, -1):
            while a%i == 0:
                res.append(i)
                a //= i
        __ a >= 10 or not res: return 0
        result = ''
        for i in range(len(res)-1, -1, -1):
            result += str(res[i])
        result = int(result)
        return result __ result < 2**31-1 else 0
    
    ___ test(self):
        testCases = [
            48,
            15,
            11,
            22,
        ]
        for num in testCases:
            print('num: %s' % num)
            result = self.smallestFactorization(num)
            print('result: %s' % result)
            print('-='*30+'-')

__ __name__ == '__main__':
    Solution().test()
