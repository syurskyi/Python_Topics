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
        __ m __ n a.. s0 != s: r.. False
        i, j = 0, 0
        flag = True
        w.... i < m a.. j < n:
            __ s0[i] __ s[j]:
                i0, j0 = i, j
                w.... i0 < m a.. s0[i0] __ s0[i]:
                    i0 += 1
                w.... j0 < n a.. s[j0] __ s[j]:
                    j0 += 1
                __ j0-j < 3 a.. s0[i:i0] != s[j:j0]:
                    flag = False
                    break
                i, j = i0, j0
            ____:
                break
        __ i __ m a.. j __ n a.. flag:
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
