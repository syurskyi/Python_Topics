'''
Created on Mar 30, 2018

@author: tongq
'''
class Solution(object
    ___ boldWords(self, words, S
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
        ___ i in range(le.(s)):
            ___ word in words:
                __ i+le.(word) <= le.(s) and s[i:i+le.(word)] __ word:
                    __ not start:
                        res += '<b>'
                        start = True
                    j = max(j, i+le.(word))
            __ i __ j and start:
                res += '</b>'
                start = False
            res += s[i]
        __ j >= le.(s
            res += '</b>'
        r_ res
    
    ___ test(self
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
        ___ words, s in testCases:
            print('words: %s' % words)
            print('s: %s' % s)
            result = self.boldWords(words, s)
            print('result: %s' % result)
            print('-='*30+'-')

__ __name__ __ '__main__':
    Solution().test()
