'''
Created on Mar 16, 2017

@author: MT
'''

class Solution(object
    ___ removeDuplicateLetters(self, s
        __ not s: r_ ''
        cnt = [0]*26
        pos = 0
        ___ c in s:
            cnt[ord(c)-ord('a')] += 1
        ___ i, c in enumerate(s
            __ s[i] < s[pos]:
                pos = i
            cnt[ord(c)-ord('a')] -= 1
            __ cnt[ord(c)-ord('a')] __ 0:
                break
        r_ s[pos]+self.removeDuplicateLetters(s[pos+1:].replace(s[pos], ''))
    
    ___ removeDuplicateLetters_another(self, s
        __ not s: r_ ''
        lastPosMap = {}
        ___ i, c in enumerate(s
            lastPosMap[c] = i
        length = le.(lastPosMap)
        res = ['a']*length
        begin, end = 0, min(lastPosMap.values())
        ___ i in range(length
            minChar = chr(ord('z')+1)
            ___ j in range(begin, end+1
                __ s[j] in lastPosMap and s[j] < minChar:
                    minChar = s[j]
                    begin = j+1
            res[i] = minChar
            __ i __ length-1:
                break
            del lastPosMap[minChar]
            end = min(lastPosMap.values())
        r_ ''.join(res)
    
    ___ test(self
        testCases = [
            'bcabc',
            'cbacbcbc',
        ]
        ___ s in testCases:
            print('s: %s' % (s))
            result = self.removeDuplicateLetters(s)
            print('result: %s' % (result))
            print('-='*20+'-')

__ __name__ __ '__main__':
    Solution().test()
