'''
Created on Mar 17, 2017

@author: MT
'''

c_ Solution(o..
    ___ maxProduct  words
        __ n.. words: r.. 0
        arr [0]*l..(words)
        ___ i, word __ e..(words
            ___ _, c __ e..(word
                arr[i] arr[i] | (1 << (o..(c) - o..('a')))
        result 0
        ___ i, word __ e..(words
            ___ j __ r..(i+1, l.. ?
                __ arr[i] & arr[j] __ 0:
                    result m..(result, l..(words[i])*l..(words[j]
        r.. ?
    
    ___ test
        testCases [
            ["abcw", "baz", "foo", "bar", "xtfn", "abcdef"],
            ["a", "ab", "abc", "d", "cd", "bcd", "abcd"],
            ["a", "aa", "aaa", "aaaa"],
        ]
        ___ words __ testCases:
            print('words: %s' % (words
            result maxProduct(words)
            print('result: %s' % (result
            print('-='*20+'-')

__ _____ __ _____
    Solution().test()
