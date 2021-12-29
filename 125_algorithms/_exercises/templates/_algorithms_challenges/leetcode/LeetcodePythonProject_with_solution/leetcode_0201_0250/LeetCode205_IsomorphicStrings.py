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
        __ len(s) != len(t):
            return False
        for c1, c2 in zip(s, t):
            __ c1 not in hashmap:
                __ c2 in hashset:
                    return False
                hashmap[c1] = c2
                hashset.add(c2)
            else:
                __ hashmap[c1] != c2:
                    return False
        return True
    
    ___ isIsomorphic_old(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        __ len(s) != len(t): return False
        hashmap1, hashmap2 = {}, {}
        for c1, c2 in zip(s, t):
            __ c1 in hashmap1 and\
            (c2 not in hashmap2 or hashmap1[c1] != c2 or hashmap2[c2] != c1):
                return False
            elif c2 in hashmap2 and\
            (c1 not in hashmap1 or hashmap1[c1] != c2 or hashmap2[c2] != c1):
                return False
            hashmap1[c1] = c2
            hashmap2[c2] = c1
        return True
    
    ___ test(self):
        testCases = [
            ('ab', 'aa'),
            ('egg', 'add'),
            ('foo', 'bar'),
            ('paper', 'title'),
        ]
        for s, t in testCases:
            print('s: %s, t: %s' % (s, t))
            result = self.isIsomorphic(s, t)
            print('result: %s' % (result))
            print('-='*20+'-')

__ __name__ == '__main__':
    Solution().test()