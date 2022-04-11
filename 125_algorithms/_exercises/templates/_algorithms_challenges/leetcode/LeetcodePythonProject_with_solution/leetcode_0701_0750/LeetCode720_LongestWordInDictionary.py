'''
Created on Jan 31, 2018

@author: tongq
'''
c_ Solution(o..
    ___ longestWord  words
        """
        :type words: List[str]
        :rtype: str
        """
        __ n.. words: r.. ''
        words.s..(key=l..)
        n l..(words[-1])
        dp [s..() ___ _ __ r..(n+1)]
        ___ word __ words:
            __ l..(word) __ 1 o. word[:-1] __ dp[l..(word)-1]:
                dp[l..(word)].add(word)
        ___ i __ r..(n, -1, -1
            __ dp[i]:
                r.. s..(l..(dp[i].p.. 0)
        r.. ''
    
    ___ test
        testCases [
            ["w","wo","wor","worl", "world"],
            ["a", "banana", "app", "appl", "ap", "apply", "apple"],
        ]
        ___ words __ testCases:
            print('words: %s' % words)
            result longestWord(words)
            print('result: %s' % result)
            print('-='*30+'-')

__ _____ __ _____
    Solution().test()
