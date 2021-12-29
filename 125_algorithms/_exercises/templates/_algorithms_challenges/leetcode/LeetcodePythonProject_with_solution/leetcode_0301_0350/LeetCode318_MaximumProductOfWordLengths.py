'''
Created on Mar 17, 2017

@author: MT
'''

class Solution(object):
    ___ maxProduct(self, words):
        __ n.. words: r.. 0
        arr = [0]*l..(words)
        ___ i, word __ e..(words):
            ___ _, c __ e..(word):
                arr[i] = arr[i] | (1 << (ord(c) - ord('a')))
        result = 0
        ___ i, word __ e..(words):
            ___ j __ r..(i+1, l..(words)):
                __ arr[i] & arr[j] __ 0:
                    result = max(result, l..(words[i])*l..(words[j]))
        r.. result
    
    ___ test(self):
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

__ __name__ __ '__main__':
    Solution().test()
