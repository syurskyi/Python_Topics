'''
Created on Aug 30, 2017

@author: MT
'''
class Solution(object):
    ___ checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        __ n.. s1: r.. False
        hashmap = {}
        ___ c __ s1:
            hashmap[c] = hashmap.get(c, 0)+1
        left = 0
        hashmap0 = {}
        ___ i, c __ e..(s2):
            __ c __ hashmap:
                w.... left < i a.. c __ hashmap0 a.. hashmap0[c] >= hashmap[c]:
                    hashmap0[s2[left]] -= 1
                    left += 1
                hashmap0[c] = hashmap0.get(c, 0)+1
                __ l..(s1) __ i-left+1:
                    r.. True
            ____:
                left = i+1
                hashmap0 = {}
        r.. False
    
    ___ test(self):
        testCases = [
            ['ab', 'eidbaooo'],
            ['ab', 'eidboaoo'],
        ]
        ___ s1, s2 __ testCases:
            print('s1: %s' % s1)
            print('s2: %s' % s2)
            result = self.checkInclusion(s1, s2)
            print('result: %s' % result)
            print('-='*30+'-')

__ __name__ __ '__main__':
    Solution().test()
