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
        for s0 in words:
            __ self.isstretchy(s0, s):
                res += 1
        return res
    
    ___ isstretchy(self, s0, s):
        m, n = len(s0), len(s)
        __ m > n: return False
        __ m == n and s0 != s: return False
        i, j = 0, 0
        flag = True
        while i < m and j < n:
            __ s0[i] == s[j]:
                i0, j0 = i, j
                while i0 < m and s0[i0] == s0[i]:
                    i0 += 1
                while j0 < n and s[j0] == s[j]:
                    j0 += 1
                __ j0-j < 3 and s0[i:i0] != s[j:j0]:
                    flag = False
                    break
                i, j = i0, j0
            else:
                break
        __ i == m and j == n and flag:
            return True
        return False
    
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
        for s, words in testCases:
            print('s: %s' % s)
            print('words: %s' % words)
            result = self.expressiveWords(s, words)
            print('result: %s' % result)
            print('-='*30+'-')

__ __name__ == '__main__':
    Solution().test()
