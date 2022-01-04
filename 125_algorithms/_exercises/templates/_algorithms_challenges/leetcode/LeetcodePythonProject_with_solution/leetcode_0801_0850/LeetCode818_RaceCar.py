'''
Created on May 1, 2018

@author: tongq
'''
c_ Solution(object):
    ___ - ):
        hashmap = {0:0}
    
    ___ racecar(self, target):
        """
        :type target: int
        :rtype: int
        """
        __ target __ hashmap: r.. hashmap[target]
        # Number of bits necessary to represent self in binary.
        n = target.bit_length()
        __ 2**n-1 __ target:
            hashmap[target] = n
        ____:
            hashmap[target] = racecar(2**n-1-target)+n+1
            ___ m __ r..(n-1):
                hashmap[target] = m..(hashmap[target],\
                            racecar(target-2**(n-1)+2**m)+n+m+1)
        r.. hashmap[target]
    
    ___ test
        testCases = [
            3,
            6,
        ]
        ___ target __ testCases:
            print('target: %s' % target)
            result = racecar(target)
            print('result: %s' % result)
            print('-='*30+'-')

__ _____ __ _____
    Solution().test()
