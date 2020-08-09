'''
Created on Mar 17, 2017

@author: MT
'''

class Solution(object
    ___ maxProduct(self, words
        __ not words: r_ 0
        arr = [0]*le.(words)
        for i, word in enumerate(words
            for _, c in enumerate(word
                arr[i] = arr[i] | (1 << (ord(c) - ord('a')))
        result = 0
        for i, word in enumerate(words
            for j in range(i+1, le.(words)):
                __ arr[i] & arr[j] __ 0:
                    result = max(result, le.(words[i])*le.(words[j]))
        r_ result
    
    ___ test(self
        testCases = [
            ["abcw", "baz", "foo", "bar", "xtfn", "abcdef"],
            ["a", "ab", "abc", "d", "cd", "bcd", "abcd"],
            ["a", "aa", "aaa", "aaaa"],
        ]
        for words in testCases:
            print('words: %s' % (words))
            result = self.maxProduct(words)
            print('result: %s' % (result))
            print('-='*20+'-')

__ __name__ __ '__main__':
    Solution().test()
