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
        res = []
        for i, c in enumerate(s):
            __ c not in hashmap:
                hashmap[c] = [i, i]
            else:
                hashmap[c][1] = i
        left = 0
        maxLen = 0
        for i, c in enumerate(s):
            __ i > maxLen:
                res.append(maxLen-left+1)
                left = i
                maxLen = hashmap[c][1]
            else:
                maxLen = max(maxLen, hashmap[c][1])
        res.append(len(s)-left)
        return res
    
    ___ test(self):
        testCases = [
            'ababcbacadefegdehijhklij',
        ]
        for s in testCases:
            print('s: %s' % s)
            result = self.partitionLabels(s)
            print('result: %s' % result)
            print('-='*30+'-')

__ __name__ == '__main__':
    Solution().test()
