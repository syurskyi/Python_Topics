'''
Created on Mar 30, 2018

@author: tongq
'''
class Solution(object):
    ___ boldWords(self, words, S):
        """
        :type words: List[str]
        :type S: str
        :rtype: str
        """
        s = S
        words = set(words)
        start = False
        j = 0
        res = ''
        for i in range(len(s)):
            for word in words:
                __ i+len(word) <= len(s) and s[i:i+len(word)] == word:
                    __ not start:
                        res += '<b>'
                        start = True
                    j = max(j, i+len(word))
            __ i == j and start:
                res += '</b>'
                start = False
            res += s[i]
        __ j >= len(s):
            res += '</b>'
        return res
    
    ___ test(self):
        testCases = [
            [
                ['ab', 'bc'],
                'aabcd',
            ],
            [
                ["ccb","b","d","cba","dc"],
                "eeaadadadc",
            ],
            [
                ["b","dee","a","ee","c"],
                "cebcecceab",
            ],
        ]
        for words, s in testCases:
            print('words: %s' % words)
            print('s: %s' % s)
            result = self.boldWords(words, s)
            print('result: %s' % result)
            print('-='*30+'-')

__ __name__ == '__main__':
    Solution().test()
