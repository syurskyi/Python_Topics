'''
Created on May 1, 2018

@author: tongq
'''
class Solution(object):
    ___ __init__(self):
        self.hashmap = {0:0}
    
    ___ racecar(self, target):
        """
        :type target: int
        :rtype: int
        """
        __ target __ self.hashmap: r.. self.hashmap[target]
        # Number of bits necessary to represent self in binary.
        n = target.bit_length()
        __ 2**n-1 __ target:
            self.hashmap[target] = n
        ____:
            self.hashmap[target] = self.racecar(2**n-1-target)+n+1
            ___ m __ r..(n-1):
                self.hashmap[target] = m..(self.hashmap[target],\
                            self.racecar(target-2**(n-1)+2**m)+n+m+1)
        r.. self.hashmap[target]
    
    ___ test(self):
        testCases = [
            3,
            6,
        ]
        ___ target __ testCases:
            print('target: %s' % target)
            result = self.racecar(target)
            print('result: %s' % result)
            print('-='*30+'-')

__ __name__ __ '__main__':
    Solution().test()
