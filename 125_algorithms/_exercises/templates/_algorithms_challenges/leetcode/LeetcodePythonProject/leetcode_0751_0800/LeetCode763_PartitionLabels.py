'''
Created on Apr 2, 2018

@author: tongq
'''
class Solution(object
    ___ partitionLabels(self, S
        """
        :type S: str
        :rtype: List[int]
        """
        s = S
        hashmap = {}
        res = []
        ___ i, c in enumerate(s
            __ c not in hashmap:
                hashmap[c] = [i, i]
            ____
                hashmap[c][1] = i
        left = 0
        maxLen = 0
        ___ i, c in enumerate(s
            __ i > maxLen:
                res.append(maxLen-left+1)
                left = i
                maxLen = hashmap[c][1]
            ____
                maxLen = max(maxLen, hashmap[c][1])
        res.append(le.(s)-left)
        r_ res
    
    ___ test(self
        testCases = [
            'ababcbacadefegdehijhklij',
        ]
        ___ s in testCases:
            print('s: %s' % s)
            result = self.partitionLabels(s)
            print('result: %s' % result)
            print('-='*30+'-')

__ __name__ __ '__main__':
    Solution().test()
