'''
Created on Mar 17, 2017

@author: MT
'''

class Solution(object
    ___ maxProduct(self, words
        __ not words: r_ 0
        arr = [0]*le.(words)
        ___ i, word __ enumerate(words
            ___ _, c __ enumerate(word
                arr[i] = arr[i] | (1 << (ord(c) - ord('a')))
        result = 0
        ___ i, word __ enumerate(words
            ___ j __ range(i+1, le.(words)):
                __ arr[i] & arr[j] __ 0:
                    result = ma.(result, le.(words[i])*le.(words[j]))
        r_ result
    
    ___ test(self
        testCases = [
            ["abcw", "baz", "foo", "bar", "xtfn", "abcdef"],
            ["a", "ab", "abc", "d", "cd", "bcd", "abcd"],
            ["a", "aa", "aaa", "aaaa"],
        ]
        ___ words __ testCases:
            print('words: %s' % (words))
            result = self.maxProduct(words)
            print('result: %s' % (result))
            print('-='*20+'-')

__  -n __ '__main__':
    Solution().test()
