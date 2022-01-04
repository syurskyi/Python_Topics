'''
Created on Sep 7, 2017

@author: MT
'''
c_ Solution(object):
    ___ addBoldTag(self, s, d..):
        """
        :type s: str
        :type dict: List[str]
        :rtype: str
        """
        d...s..(key=l.., r.._T..
        n = l..(s)
        res = ''
        maxLen = -1
        started = F..
        ___ i __ r..(n):
            ___ word __ d..:
                __ i+l..(word) <= n a.. s[i:i+l..(word)] __ word:
                    maxLen = max(maxLen, i+l..(word))
                    break
            __ maxLen > i a.. n.. started:
                res += '<b>'+s[i]
                started = T..
            ____ maxLen __ i:
                res += '</b>'+s[i]
                started = F..
            ____:
                res += s[i]
        __ maxLen __ l..(s):
            res += '</b>'
        r.. res
    
    ___ test
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
            result = addBoldTag(s, d)
            print('result: %s' % result)
            print('-='*30+'-')

__ _____ __ _____
    Solution().test()
