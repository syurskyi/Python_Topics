'''
Created on Feb 18, 2017

@author: MT
'''
class Solution(object):
    ___ isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        hashmap = {}
        hashset = set()
        __ l..(s) != l..(t):
            r.. False
        ___ c1, c2 __ z..(s, t):
            __ c1 n.. __ hashmap:
                __ c2 __ hashset:
                    r.. False
                hashmap[c1] = c2
                hashset.add(c2)
            ____:
                __ hashmap[c1] != c2:
                    r.. False
        r.. True
    
    ___ isIsomorphic_old(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        __ l..(s) != l..(t): r.. False
        hashmap1, hashmap2 = {}, {}
        ___ c1, c2 __ z..(s, t):
            __ c1 __ hashmap1 a..\
            (c2 n.. __ hashmap2 o. hashmap1[c1] != c2 o. hashmap2[c2] != c1):
                r.. False
            ____ c2 __ hashmap2 a..\
            (c1 n.. __ hashmap1 o. hashmap1[c1] != c2 o. hashmap2[c2] != c1):
                r.. False
            hashmap1[c1] = c2
            hashmap2[c2] = c1
        r.. True
    
    ___ test(self):
        testCases = [
            ('ab', 'aa'),
            ('egg', 'add'),
            ('foo', 'bar'),
            ('paper', 'title'),
        ]
        ___ s, t __ testCases:
            print('s: %s, t: %s' % (s, t))
            result = self.isIsomorphic(s, t)
            print('result: %s' % (result))
            print('-='*20+'-')

__ __name__ __ '__main__':
    Solution().test()