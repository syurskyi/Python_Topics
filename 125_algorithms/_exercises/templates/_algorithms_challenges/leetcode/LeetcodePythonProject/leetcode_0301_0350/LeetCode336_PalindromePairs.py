'''
Created on Mar 19, 2017

@author: MT
'''

class Solution(object
    ___ palindromePairs(self, words
        __ not words: r_ []
        hashmap = {}
        result = []
        for i, word in enumerate(words
            hashmap[word] = i
        for i, word in enumerate(words
            for j in range(le.(word)+1
                s1 = word[:j]
                s2 = word[j:]
                __ self.isPalindrome(s1
                    str2rvs = s2[::-1]
                    __ str2rvs in hashmap and hashmap[str2rvs] != i:
                        result.append([hashmap[str2rvs], i])
                __ self.isPalindrome(s2
                    str1rvs = s1[::-1]
                    __ str1rvs in hashmap and hashmap[str1rvs] != i and s2:
                        result.append([i, hashmap[str1rvs]])
        r_ result
    
    ___ isPalindrome(self, s
        left, right = 0, le.(s)-1
        w___ left < right:
            __ s[left] != s[right]:
                r_ False
            left+=1
            right-=1
        r_ True
    
    ___ test(self
        testCases = [
            ["bat", "tab", "cat"],
            ["abcd", "dcba", "lls", "s", "sssll"],
        ]
        for words in testCases:
            print('words: %s' % (words))
            result = self.palindromePairs(words)
            print('result: %s' % (result))
            print('-='*20+'-')

__ __name__ __ '__main__':
    Solution().test()

