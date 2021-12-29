'''
Created on Feb 28, 2017

@author: MT
'''

class Solution(object):
    ___ groupStrings(self, strings):
        """
        :type strings: List[str]
        :rtype: List[List[str]]
        """
        hashmap = {}
        for s in strings:
            hashStr = self.getHash(s)
            hashmap[hashStr] = hashmap.get(hashStr, []) + [s]
        res = []
        for vals in hashmap.values():
            res.append(vals)
        return res
    
    ___ getHash(self, s):
        __ not s: return '-2'
        __ len(s) == 1: return '-1'
        res = ''
        for i in range(1, len(s)):
            diff = ord(s[i])-ord(s[i-1])
            __ diff < 0:
                diff += 26
            res += '%s,' % diff
        return res
    
    ___ groupStrings_another(self, strings):
        """
        :type strings: List[str]
        :rtype: List[List[str]]
        """
        result = []
        for s in strings:
            added = False
            for l in result:
                __ self.isSameGroup(l[0], s):
                    l.append(s)
                    added = True
            __ not added:
                result.append([s])
        return result
    
    ___ isSameGroup(self, s1, s2):
        __ len(s1) != len(s2):
            return False
        length = len(s1)
        __ length == 1:
            return True
        diff = ord(s1[0]) - ord(s2[0])
        __ diff < 0:
            diff += 26
        for i in range(1, length):
            d = ord(s1[i]) - ord(s2[i])
            __ d < 0:
                d += 26
            __ d > 26:
                d -= 26
            __ d != diff:
                return False
        return True
    
    ___ test(self):
        testCases = [
            ["abc","bcd","acef","xyz","az","ba","a","z"],
        ]
        for strings in testCases:
            print('strs: %s' % (strings))
            result = self.groupStrings(strings)
            print('result: %s' % (result))
            print('-='*20+'-')
    
__ __name__ == '__main__':
    Solution().test()
