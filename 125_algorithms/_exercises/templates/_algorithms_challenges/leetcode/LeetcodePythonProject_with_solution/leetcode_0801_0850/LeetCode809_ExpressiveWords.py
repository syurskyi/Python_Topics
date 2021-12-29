'''
Created on Apr 25, 2018

@author: tongq
'''
class Solution(object):
    ___ expressiveWords(self, S, words):
        """
        :type S: str
        :type words: List[str]
        :rtype: int
        """
        s = S
        res = 0
        ___ s0 __ words:
            __ self.isstretchy(s0, s):
                res += 1
        r.. res
    
    ___ isstretchy(self, s0, s):
        m, n = l..(s0), l..(s)
        __ m > n: r.. False
        __ m __ n and s0 != s: r.. False
        i, j = 0, 0
        flag = True
        while i < m and j < n:
            __ s0[i] __ s[j]:
                i0, j0 = i, j
                while i0 < m and s0[i0] __ s0[i]:
                    i0 += 1
                while j0 < n and s[j0] __ s[j]:
                    j0 += 1
                __ j0-j < 3 and s0[i:i0] != s[j:j0]:
                    flag = False
                    break
                i, j = i0, j0
            ____:
                break
        __ i __ m and j __ n and flag:
            r.. True
        r.. False
    
    ___ test(self):
        testCases = [
            [
                "heeellooo",
                ["hello", "hi", "helo"]
            ],
            [
                "zzzzzyyyyy",
                ["zzyy","zy","zyy"],
            ],
            [
                "dddiiiinnssssssoooo",
                ["dinnssoo","ddinso","ddiinnso","ddiinnssoo","ddiinso","dinsoo","ddiinsso","dinssoo","dinso"],
#                 ["dinnssoo"],
            ],
        ]
        ___ s, words __ testCases:
            print('s: %s' % s)
            print('words: %s' % words)
            result = self.expressiveWords(s, words)
            print('result: %s' % result)
            print('-='*30+'-')

__ __name__ __ '__main__':
    Solution().test()
