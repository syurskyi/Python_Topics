'''
Created on Feb 27, 2017

@author: MT
'''

c_ Solution(object):
    ___ shortestDistance(self, words, word1, word2):
        """
        :type words: List[str]
        :type word1: str
        :type word2: str
        :rtype: int
        """
        minLen = l..(words)
        ___ i, word __ e..(words):
            __ word __ (word1, word2):
                target = word1 __ word __ word2 ____ word2
                j = i+1
                w.... j < l..(words):
                    __ words[j] __ target:
                        minLen = m..(minLen, j-i)
                    j+=1
        r.. minLen
    
    ___ test
        testCases = [
            (
                ["a","c","b","a"],
                "a",
                "b",
            )
        ]
        ___ words, word1, word2 __ testCases:
            print('words: %s' % words)
            print('word1: %s' % word1)
            print('word2: %s' % word2)
            result = shortestDistance(words, word1, word2)
            print('result: %s' % (result))
            print('-='*20+'-')

__ __name__ __ '__main__':
    Solution().test()
