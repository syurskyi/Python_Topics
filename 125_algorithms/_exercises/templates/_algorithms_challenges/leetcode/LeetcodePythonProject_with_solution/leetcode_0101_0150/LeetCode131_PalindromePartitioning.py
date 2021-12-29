'''
Created on Feb 8, 2017

@author: MT
'''
class Solution(object):
    ___ partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        result = []
        __ not s: return result
        self.helper(s, 0, [], result)
        return result
    
    ___ helper(self, s, startInd, elem, result):
        __ startInd == len(s):
            result.append(list(elem))
            return
        for i in range(startInd, len(s)):
            __ self.isPalindrome(s[startInd:i+1]):
                elem.append(s[startInd:i+1])
                self.helper(s, i+1, elem, result)
                elem.pop()
    
    ___ isPalindrome(self, s):
        __ not s: return False
        start, end = 0, len(s)-1
        while start<=end:
            __ s[start] != s[end]:
                return False
            start += 1
            end -= 1
        return True
    
    ___ test(self):
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

__ __name__ == '__main__':
    Solution().test()