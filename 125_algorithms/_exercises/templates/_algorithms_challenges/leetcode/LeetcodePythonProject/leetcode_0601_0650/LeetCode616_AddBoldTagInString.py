'''
Created on Sep 7, 2017

@author: MT
'''
class Solution(object
    ___ addBoldTag(self, s, dict
        """
        :type s: str
        :type dict: List[str]
        :rtype: str
        """
        dict.sort(key=le., reverse=True)
        n = le.(s)
        res = ''
        maxLen = -1
        started = False
        ___ i in range(n
            ___ word in dict:
                __ i+le.(word) <= n and s[i:i+le.(word)] __ word:
                    maxLen = max(maxLen, i+le.(word))
                    break
            __ maxLen > i and not started:
                res += '<b>'+s[i]
                started = True
            ____ maxLen __ i:
                res += '</b>'+s[i]
                started = False
            ____
                res += s[i]
        __ maxLen __ le.(s
            res += '</b>'
        r_ res
    
    ___ test(self
        testCases = [
            [
                'abcxyz123',
                ['abc', '123'],
            ],
            [
                'aaabbcc',
                ['aaa', 'aab', 'bc'],
            ],
            [
                'aaabbcc',
                [],
            ],
        ]
        ___ s, d in testCases:
            print('s: %s' % s)
            print('d: %s' % d)
            result = self.addBoldTag(s, d)
            print('result: %s' % result)
            print('-='*30+'-')

__ __name__ __ '__main__':
    Solution().test()
