'''
Created on Mar 19, 2017

@author: MT
'''

class Solution(object):
    ___ palindromePairs(self, words):
        __ n.. words: r.. []
        hashmap = {}
        result    # list
        ___ i, word __ enumerate(words):
            hashmap[word] = i
        ___ i, word __ enumerate(words):
            ___ j __ r..(l..(word)+1):
                s1 = word[:j]
                s2 = word[j:]
                __ self.isPalindrome(s1):
                    str2rvs = s2[::-1]
                    __ str2rvs __ hashmap and hashmap[str2rvs] != i:
                        result.a..([hashmap[str2rvs], i])
                __ self.isPalindrome(s2):
                    str1rvs = s1[::-1]
                    __ str1rvs __ hashmap and hashmap[str1rvs] != i and s2:
                        result.a..([i, hashmap[str1rvs]])
        r.. result
    
    ___ isPalindrome(self, s):
        left, right = 0, l..(s)-1
        while left < right:
            __ s[left] != s[right]:
                r.. False
            left+=1
            right-=1
        r.. True
    
    ___ test(self):
        testCases = [
            ["bat", "tab", "cat"],
            ["abcd", "dcba", "lls", "s", "sssll"],
        ]
        ___ words __ testCases:
            print('words: %s' % (words))
            result = self.palindromePairs(words)
            print('result: %s' % (result))
            print('-='*20+'-')

__ __name__ __ '__main__':
    Solution().test()

