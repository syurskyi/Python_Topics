'''
Created on Feb 8, 2017

@author: MT
'''
class Solution(object
    ___ partition(self, s
        """
        :type s: str
        :rtype: List[List[str]]
        """
        result = []
        __ not s: r_ result
        self.helper(s, 0, [], result)
        r_ result
    
    ___ helper(self, s, startInd, elem, result
        __ startInd __ le.(s
            result.append(list(elem))
            r_
        for i in range(startInd, le.(s)):
            __ self.isPalindrome(s[startInd:i+1]
                elem.append(s[startInd:i+1])
                self.helper(s, i+1, elem, result)
                elem.pop()
    
    ___ isPalindrome(self, s
        __ not s: r_ False
        start, end = 0, le.(s)-1
        w___ start<=end:
            __ s[start] != s[end]:
                r_ False
            start += 1
            end -= 1
        r_ True
    
    ___ test(self
        testCases = [
            'aab',
            'aabbcc',
            'abcba',
        ]
        for s in testCases:
            print('s: %s' % (s))
            result = self.partition(s)
            print('result: %s' % (result))
            print('-='*20+'-')

__ __name__ __ '__main__':
    Solution().test()