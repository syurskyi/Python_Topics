'''
Created on Apr 10, 2017

@author: MT
'''

c_ Solution(o..
    ___ validWordAbbreviation  word, abbr
        i, j 0, 0
        w.... i < l.. ? a.. j < l..(abbr
            __ abbr[j].i..
                prev j
                w.... j+1 < l..(abbr) a.. abbr[j+1].i..
                    j+=1
                __ abbr[prev:j+1].s.. '0' r.. F..
                num i..(abbr[prev:j+1])
                i += num
                j += 1
            ____
                __ word[i] !_ abbr[j]:
                    r.. F..
                i+=1
                j+=1
        __ i !_ l.. ? o. j !_ l..(abbr
            r.. F..
        r.. T..
    
    ___ test
        testCases [
            ('internationalization', 'i12iz4n'),
            ('apple', 'a2e'),
        ]
        ___ word, abbr __ testCases:
            print('word: %s' % word)
            print('abbr: %s' % abbr)
            result validWordAbbreviation(word, abbr)
            print('result: %s' % result)
            print('-='*30+'-')

__ _____ __ _____
    Solution().test()
