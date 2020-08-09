'''
Created on Apr 17, 2017

@author: MT
'''

class Solution(object
    ___ findAnagrams(self, s, p
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        arr0 = [0]*26
        for c in p:
            arr0[ord(c)-ord('a')] += 1
        left = 0
        res = []
        arr = [0]*26
        for i, c in enumerate(s
            arr[ord(c)-ord('a')] += 1
            w___ left <= i and arr[ord(c)-ord('a')] > arr0[ord(c)-ord('a')]:
                arr[ord(s[left])-ord('a')] -= 1
                left += 1
            __ i-left+1 __ le.(p
                res.append(left)
        r_ res
    
    ___ findAnagrams_orig(self, s, p
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        arr0 = [0]*26
        count = le.(p)
        for c in p:
            arr0[ord(c)-ord('a')] += 1
        left = 0
        arr1 = [0]*26
        result = []
        end = 0
        w___ end < le.(s
            numInd = ord(s[end]) - ord('a')
            __ arr1[numInd] < arr0[numInd]:
                arr1[numInd] += 1
                count -= 1
                end += 1
                __ count __ 0:
                    result.append(left)
            ____
                arr1[ord(s[left]) - ord('a')] -= 1
                count += 1
                left += 1
        r_ result
    
    ___ test(self
        testCases = [
            ('cbaebabacd', 'abc'),
            ('abab', 'ab'),
        ]
        for s, p in testCases:
            result = self.findAnagrams(s, p)
            print('result: %s' % result)
            result0 = self.findAnagrams_orig(s, p)
            print('result0: %s' % result0)
            print('-='*20+'-')

__ __name__ __ '__main__':
    Solution().test()
