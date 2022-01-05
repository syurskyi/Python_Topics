'''
Created on Mar 16, 2017

@author: MT
'''

c_ Solution(object):
    ___ removeDuplicateLetters  s):
        __ n.. s: r.. ''
        cnt = [0]*26
        pos = 0
        ___ c __ s:
            cnt[o..(c)-o..('a')] += 1
        ___ i, c __ e..(s):
            __ s[i] < s[pos]:
                pos = i
            cnt[o..(c)-o..('a')] -= 1
            __ cnt[o..(c)-o..('a')] __ 0:
                break
        r.. s[pos]+removeDuplicateLetters(s[pos+1:].r..(s[pos], ''))
    
    ___ removeDuplicateLetters_another  s):
        __ n.. s: r.. ''
        lastPosMap    # dict
        ___ i, c __ e..(s):
            lastPosMap[c] = i
        length = l..(lastPosMap)
        res = ['a']*length
        begin, end = 0, m..(lastPosMap.values())
        ___ i __ r..(length):
            minChar = chr(o..('z')+1)
            ___ j __ r..(begin, end+1):
                __ s[j] __ lastPosMap a.. s[j] < minChar:
                    minChar = s[j]
                    begin = j+1
            res[i] = minChar
            __ i __ length-1:
                break
            del lastPosMap[minChar]
            end = m..(lastPosMap.values())
        r.. ''.j..(res)
    
    ___ test
        testCases = [
            'bcabc',
            'cbacbcbc',
        ]
        ___ s __ testCases:
            print('s: %s' % (s))
            result = removeDuplicateLetters(s)
            print('result: %s' % (result))
            print('-='*20+'-')

__ _____ __ _____
    Solution().test()
