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
        ___ i __ r..(l..(s)):
            ___ word __ words:
                __ i+l..(word) <= l..(s) a.. s[i:i+l..(word)] __ word:
                    __ n.. start:
                        res += '<b>'
                        start = True
                    j = max(j, i+l..(word))
            __ i __ j a.. start:
                res += '</b>'
                start = False
            res += s[i]
        __ j >= l..(s):
            res += '</b>'
        r.. res
    
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
        ___ words, s __ testCases:
            print('words: %s' % words)
            print('s: %s' % s)
            result = self.boldWords(words, s)
            print('result: %s' % result)
            print('-='*30+'-')

__ __name__ __ '__main__':
    Solution().test()
