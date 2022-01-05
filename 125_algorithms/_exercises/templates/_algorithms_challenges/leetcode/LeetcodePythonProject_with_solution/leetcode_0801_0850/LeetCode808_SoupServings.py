'''
Created on Apr 25, 2018

@author: tongq
'''
c_ Solution(o..):
    ___ soupServings  N):
        """
        :type N: int
        :rtype: float
        """
        n = N
        hashmap    # dict
        __ N < 5000:
            r.. helper(hashmap, n, n)
        ____:
            r.. 1
    
    ___ helper  hashmap, a, b):
        __ a <= 0 a.. b <= 0:
            r.. 0.5
        __ a <= 0:
            r.. 1
        __ b <= 0:
            r.. 0
        s = s..(a)+':'+s..(b)
        __ s n.. __ hashmap:
            hashmap[s] = 0.25*(
                    helper(hashmap, a-100, b)+\
                    helper(hashmap, a-25, b-75)+\
                    helper(hashmap, a-75, b-25)+\
                    helper(hashmap, a-50, b-50)
                )
        r.. hashmap[s]
    
    ___ test
        testCases = [
            50,
        ]
        ___ n __ testCases:
            result = soupServings(n)
            print('result: %s' % result)
            print('-='*30+'-')

__ _____ __ _____
    Solution().test()
