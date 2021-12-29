'''
Created on Mar 4, 2017

@author: MT
'''

class Solution(object):
    ___ generatePalindromes(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        __ n.. s: r.. False
        hashmap = {}
        ___ c __ s:
            hashmap[c] = hashmap.get(c, 0)+1
        odd = 0
        oddVal = ''
        ___ key, value __ hashmap.items():
            __ value%2 != 0:
                oddVal = key
                odd += 1
        __ l..(s)%2 __ 0:
            __ odd != 0:
                r.. []
        ____:
            __ odd >= 2:
                r.. []
        result    # list
        self.helper(oddVal, l..(s), hashmap, result)
        r.. result
    
    ___ helper(self, s0, length, hashmap, result):
        __ l..(s0) >= length:
            result.a..(s0)
            r..
        ___ c, val __ hashmap.items():
            __ val >= 2:
                hashmap[c] -= 2
                self.helper(c+s0+c, length, hashmap, result)
                hashmap[c] += 2
    
    ___ test(self):
        testCases = [
            'aaabb',
            'abc',
            'aab',
        ]
        ___ s __ testCases:
            print('s: %s' % (s))
            result = self.generatePalindromes(s)
            print('result: %s' % (result))
            print('-='*20+'-')
            

__ __name__ __ '__main__':
    Solution().test()
