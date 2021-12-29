'''
Created on Sep 7, 2017

@author: MT
'''
class Solution(object):
    ___ addBoldTag(self, s, d..):
        """
        :type s: str
        :type dict: List[str]
        :rtype: str
        """
        d...sort(key=l.., r.._T..
        n = l..(s)
        res = ''
        maxLen = -1
        started = False
        ___ i __ r..(n):
            ___ word __ d..:
                __ i+l..(word) <= n and s[i:i+l..(word)] __ word:
                    maxLen = max(maxLen, i+l..(word))
                    break
            __ maxLen > i and n.. started:
                res += '<b>'+s[i]
                started = True
            ____ maxLen __ i:
                res += '</b>'+s[i]
                started = False
            ____:
                res += s[i]
        __ maxLen __ l..(s):
            res += '</b>'
        r.. res
    
    ___ test(self):
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
        ___ s, d __ testCases:
            print('s: %s' % s)
            print('d: %s' % d)
            result = self.addBoldTag(s, d)
            print('result: %s' % result)
            print('-='*30+'-')

__ __name__ __ '__main__':
    Solution().test()
