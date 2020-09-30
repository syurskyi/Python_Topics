'''
Created on May 1, 2018

@author: tongq
'''
class Solution(object
    ___ ambiguousCoordinates(self, S
        """
        :type S: str
        :rtype: List[str]
        """
        s = S
        n = le.(s)
        res =   # list
        ___ i __ range(1, n-2
            arrA = self.helper(s[1:i+1])
            arrB = self.helper(s[i+1:n-1])
            ___ s1 __ arrA:
                ___ s2 __ arrB:
                    res.append('(%s, %s)' % (s1, s2))
        r_ res
    
    ___ helper(self, s
        n = le.(s)
        res =   # list
        __ n __ 0 or (n > 1 and s[0] __ '0' and s[-1] __ '0'
            r_ res
        __ n > 1 and s[0] __ '0':
            res.append('0.'+s[1:])
            r_ res
        res.append(s)
        __ n __ 1 or s[-1] __ '0':
            r_ res
        ___ i __ range(1, n
            res.append(s[:i]+'.'+s[i:])
        r_ res
    
    ___ test(self
        testCases = [
            '(123)',
            '(00011)',
            '(0123)',
            '(100)',
        ]
        ___ s __ testCases:
            print('s: %s' % s)
            result = self.ambiguousCoordinates(s)
            print('result: %s' % result)
            print('-='*30+'-')

__  -n __ '__main__':
    Solution().test()
