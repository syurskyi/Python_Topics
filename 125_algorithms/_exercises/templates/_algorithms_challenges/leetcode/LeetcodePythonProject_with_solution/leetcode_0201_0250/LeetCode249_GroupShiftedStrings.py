'''
Created on Feb 28, 2017

@author: MT
'''

c_ Solution(object):
    ___ groupStrings(self, strings):
        """
        :type strings: List[str]
        :rtype: List[List[str]]
        """
        hashmap    # dict
        ___ s __ strings:
            hashStr = getHash(s)
            hashmap[hashStr] = hashmap.get(hashStr, []) + [s]
        res    # list
        ___ vals __ hashmap.v..
            res.a..(vals)
        r.. res
    
    ___ getHash(self, s):
        __ n.. s: r.. '-2'
        __ l..(s) __ 1: r.. '-1'
        res = ''
        ___ i __ r..(1, l..(s)):
            diff = ord(s[i])-ord(s[i-1])
            __ diff < 0:
                diff += 26
            res += '%s,' % diff
        r.. res
    
    ___ groupStrings_another(self, strings):
        """
        :type strings: List[str]
        :rtype: List[List[str]]
        """
        result    # list
        ___ s __ strings:
            added = F..
            ___ l __ result:
                __ isSameGroup(l[0], s):
                    l.a..(s)
                    added = T..
            __ n.. added:
                result.a..([s])
        r.. result
    
    ___ isSameGroup(self, s1, s2):
        __ l..(s1) != l..(s2):
            r.. F..
        length = l..(s1)
        __ length __ 1:
            r.. T..
        diff = ord(s1[0]) - ord(s2[0])
        __ diff < 0:
            diff += 26
        ___ i __ r..(1, length):
            d = ord(s1[i]) - ord(s2[i])
            __ d < 0:
                d += 26
            __ d > 26:
                d -= 26
            __ d != diff:
                r.. F..
        r.. T..
    
    ___ test
        testCases = [
            ["abc","bcd","acef","xyz","az","ba","a","z"],
        ]
        ___ strings __ testCases:
            print('strs: %s' % (strings))
            result = groupStrings(strings)
            print('result: %s' % (result))
            print('-='*20+'-')
    
__ __name__ __ '__main__':
    Solution().test()
