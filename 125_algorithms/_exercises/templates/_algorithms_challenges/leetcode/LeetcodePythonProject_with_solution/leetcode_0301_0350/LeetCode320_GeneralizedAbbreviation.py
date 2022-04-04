'''
Created on Mar 17, 2017

@author: MT
'''

c_ Solution(o..
    ___ generateAbbreviations  word
        """
        :type word: str
        :rtype: List[str]
        """
        res    # list
        helper(word, 0, 0, '', res)
        r.. res
    
    ___ helper  word, i, count, curr, res
        __ i __ l..(word
            __ count:
                curr += s..(count)
            res.a..(curr)
            r..
        helper(word, i+1, count+1, curr, res)
        __ count:
            helper(word, i+1, 0, curr+s..(count)+word[i], res)
        ____
            helper(word, i+1, 0, curr+word[i], res)
    
    ___ test
        testCases = [
            'word',
        ]
        ___ word __ testCases:
            print('word: %s' % (word
            result = generateAbbreviations(word)
            print('result: %s' % (result
            print('-='*20+'-')

__ _____ __ _____
    Solution().test()

