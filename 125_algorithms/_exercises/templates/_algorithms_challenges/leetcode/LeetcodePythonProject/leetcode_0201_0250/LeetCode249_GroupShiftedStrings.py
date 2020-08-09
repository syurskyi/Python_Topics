'''
Created on Feb 28, 2017

@author: MT
'''

class Solution(object
    ___ groupStrings(self, strings
        """
        :type strings: List[str]
        :rtype: List[List[str]]
        """
        hashmap = {}
        ___ s in strings:
            hashStr = self.getHash(s)
            hashmap[hashStr] = hashmap.get(hashStr, []) + [s]
        res = []
        ___ vals in hashmap.values(
            res.append(vals)
        r_ res
    
    ___ getHash(self, s
        __ not s: r_ '-2'
        __ le.(s) __ 1: r_ '-1'
        res = ''
        ___ i in range(1, le.(s)):
            diff = ord(s[i])-ord(s[i-1])
            __ diff < 0:
                diff += 26
            res += '%s,' % diff
        r_ res
    
    ___ groupStrings_another(self, strings
        """
        :type strings: List[str]
        :rtype: List[List[str]]
        """
        result = []
        ___ s in strings:
            added = False
            ___ l in result:
                __ self.isSameGroup(l[0], s
                    l.append(s)
                    added = True
            __ not added:
                result.append([s])
        r_ result
    
    ___ isSameGroup(self, s1, s2
        __ le.(s1) != le.(s2
            r_ False
        length = le.(s1)
        __ length __ 1:
            r_ True
        diff = ord(s1[0]) - ord(s2[0])
        __ diff < 0:
            diff += 26
        ___ i in range(1, length
            d = ord(s1[i]) - ord(s2[i])
            __ d < 0:
                d += 26
            __ d > 26:
                d -= 26
            __ d != diff:
                r_ False
        r_ True
    
    ___ test(self
        testCases = [
            ["abc","bcd","acef","xyz","az","ba","a","z"],
        ]
        ___ strings in testCases:
            print('strs: %s' % (strings))
            result = self.groupStrings(strings)
            print('result: %s' % (result))
            print('-='*20+'-')
    
__ __name__ __ '__main__':
    Solution().test()
