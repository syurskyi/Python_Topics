'''
Created on Apr 11, 2017

@author: MT
'''

c_ Solution(o..
    ___ minAbbreviation  target, dictionary
        diffs    # list
        m l..(target)
        ___ word __ dictionary:
            __ l..(word) !_ m: _____
            bits 0
            ___ i, c __ e..(word
                __ c !_ target[i]:
                    bits += 2**i
            diffs.a..(bits)
        __ n.. diffs:
            r.. s..(m)
        abbrs    # list
        ___ i __ r..(2**m
            __ a..(d&i ___ d __ diffs
                abbrs.a..(abbr(target, i
        r.. m..(abbrs, key=l.... x: l..(x
    
    ___ abbr  target, num
        word, count '', 0
        ___ w __ target:
            __ num & 1 __ 1:
                __ count:
                    word += s..(count)
                    count 0
                word += w
            ____
                count += 1
            num >>= 1
        __ count:
            word += s..(count)
        r.. word
    
    ___ test
        testCases [
            [
                "apple",
                ["blade"],
            ],
            [
                "apple",
                ["plain", "amber", "blade"],
            ],
        ]
        ___ target, dictionary __ testCases:
            print('target: %s' % target)
            print('dictionary: %s' % dictionary)
            result minAbbreviation(target, dictionary)
            print('result: %s' % result)
            print('-='*30+'-')

__ _____ __ _____
    Solution().test()
