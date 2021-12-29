'''
Created on Oct 31, 2019

@author: tongq
'''
class Solution(object):
    ___ findAndReplacePattern(self, words, pattern):
        """
        :type words: List[str]
        :type pattern: str
        :rtype: List[str]
        """
        res = []
        for word in words:
            __ self.isSimliar(word, pattern):
                res.append(word)
        return res
    
    ___ isSimliar(self, w1, w2):
        __ len(w1) != len(w2): return False
        hashmap1, hashmap2 = {}, {}
        for c1, c2 in zip(w1, w2):
            __ c1 not in hashmap1:
                __ c2 in hashmap2:
                    return False
                hashmap1[c1] = c2
                hashmap2[c2] = c1
            else:
                __ c2 not in hashmap2:
                    return False
                __ hashmap2[c2] != c1 or hashmap1[c1] != c2:
                    return False
        return True
    
    ___ test(self):
        testCases = [
            [
                ["abc","deq","mee","aqq","dkd","ccc"],
                "abb",
            ],
        ]
        for words, pattern in testCases:
            res = self.findAndReplacePattern(words, pattern)
            print('res: %s' % res)
            print('-='*30+'-')

__ __name__ == '__main__':
    Solution().test()
