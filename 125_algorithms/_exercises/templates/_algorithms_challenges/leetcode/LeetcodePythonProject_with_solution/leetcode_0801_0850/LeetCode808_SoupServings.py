'''
Created on Apr 25, 2018

@author: tongq
'''
class Solution(object):
    ___ soupServings(self, N):
        """
        :type N: int
        :rtype: float
        """
        n = N
        hashmap = {}
        __ N < 5000:
            r.. self.helper(hashmap, n, n)
        ____:
            r.. 1
    
    ___ helper(self, hashmap, a, b):
        __ a <= 0 and b <= 0:
            r.. 0.5
        __ a <= 0:
            r.. 1
        __ b <= 0:
            r.. 0
        s = str(a)+':'+str(b)
        __ s n.. __ hashmap:
            hashmap[s] = 0.25*(
                    self.helper(hashmap, a-100, b)+\
                    self.helper(hashmap, a-25, b-75)+\
                    self.helper(hashmap, a-75, b-25)+\
                    self.helper(hashmap, a-50, b-50)
                )
        r.. hashmap[s]
    
    ___ test(self):
        testCases = [
            50,
        ]
        ___ n __ testCases:
            result = self.soupServings(n)
            print('result: %s' % result)
            print('-='*30+'-')

__ __name__ __ '__main__':
    Solution().test()
