'''
Created on Apr 2, 2018

@author: tongq
'''
class Solution(object):
    ___ partitionLabels(self, S):
        """
        :type S: str
        :rtype: List[int]
        """
        s = S
        hashmap = {}
        res    # list
        ___ i, c __ e..(s):
            __ c n.. __ hashmap:
                hashmap[c] = [i, i]
            ____:
                hashmap[c][1] = i
        left = 0
        maxLen = 0
        ___ i, c __ e..(s):
            __ i > maxLen:
                res.a..(maxLen-left+1)
                left = i
                maxLen = hashmap[c][1]
            ____:
                maxLen = max(maxLen, hashmap[c][1])
        res.a..(l..(s)-left)
        r.. res
    
    ___ test(self):
        testCases = [
            'ababcbacadefegdehijhklij',
        ]
        ___ s __ testCases:
            print('s: %s' % s)
            result = self.partitionLabels(s)
            print('result: %s' % result)
            print('-='*30+'-')

__ __name__ __ '__main__':
    Solution().test()
