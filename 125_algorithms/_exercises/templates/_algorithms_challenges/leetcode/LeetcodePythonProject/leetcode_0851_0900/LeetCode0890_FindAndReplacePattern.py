'''
Created on Oct 31, 2019

@author: tongq
'''
class Solution(object
    ___ findAndReplacePattern(self, words, pattern
        """
        :type words: List[str]
        :type pattern: str
        :rtype: List[str]
        """
        res =   # list
        ___ word __ words:
            __ self.isSimliar(word, pattern
                res.append(word)
        r_ res
    
    ___ isSimliar(self, w1, w2
        __ le.(w1) != le.(w2 r_ False
        hashmap1, hashmap2 = {}, {}
        ___ c1, c2 __ zip(w1, w2
            __ c1 not __ hashmap1:
                __ c2 __ hashmap2:
                    r_ False
                hashmap1[c1] = c2
                hashmap2[c2] = c1
            ____
                __ c2 not __ hashmap2:
                    r_ False
                __ hashmap2[c2] != c1 or hashmap1[c1] != c2:
                    r_ False
        r_ True
    
    ___ test(self
        testCases = [
            [
                ["abc","deq","mee","aqq","dkd","ccc"],
                "abb",
            ],
        ]
        ___ words, pattern __ testCases:
            res = self.findAndReplacePattern(words, pattern)
            print('res: %s' % res)
            print('-='*30+'-')

__  -n __ '__main__':
    Solution().test()
