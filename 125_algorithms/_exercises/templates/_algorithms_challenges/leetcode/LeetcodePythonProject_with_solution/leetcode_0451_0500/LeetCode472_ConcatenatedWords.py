'''
Created on Apr 26, 2017

@author: MT
'''

c_ Solution(object):
    ___ findAllConcatenatedWordsInADict(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        res    # list
        words.s..(key=l..)
        hashset = set()
        ___ word __ words:
            __ helper(hashset, word):
                res.a..(word)
            hashset.add(word)
        r.. res
    
    ___ helper(self, hashset, word1):
        __ n.. hashset: r.. F..
        dp = [F..]*(l..(word1)+1)
        dp[0] = T..
        ___ i __ r..(1, l..(word1)+1):
            ___ j __ r..(i):
                __ dp[j]:
                    __ word1[j:i] __ hashset:
                        dp[i] = T..
                        break
        r.. dp[-1]
    
    ___ test
        testCases =[
            [''],
            ["cat","cats","catsdogcats","dog","dogcatsdog","hippopotamuses","rat","ratcatdogcat"],
        ]
        ___ words __ testCases:
            print('words: %s' % words)
            result = findAllConcatenatedWordsInADict(words)
            print('result: %s' % result)
            print('-='*20+'-')

__ __name__ __ '__main__':
    Solution().test()
