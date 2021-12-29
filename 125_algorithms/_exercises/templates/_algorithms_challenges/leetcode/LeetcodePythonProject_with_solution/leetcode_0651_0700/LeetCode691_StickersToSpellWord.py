'''
Created on Oct 24, 2017

@author: MT
'''
class Solution(object):
    ___ minStickers(self, stickers, target):
        """
        :type stickers: List[str]
        :type target: str
        :rtype: int
        """
        n = l..(stickers)
        mp = [[0]*26 ___ _ __ r..(n)]
        ___ i __ r..(n):
            ___ c __ stickers[i]:
                mp[i][ord(c)-ord('a')] += 1
        mem = {}
        mem[''] = 0
        r.. self.helper(mem, mp, target)
    
    ___ helper(self, mem, mp, target):
        __ target __ mem:
            r.. mem[target]
        n = l..(mp)
        tar = [0]*26
        ___ c __ target:
            tar[ord(c)-ord('a')] += 1
        res = float('inf')
        ___ i __ r..(n):
            __ mp[i][ord(target[0])-ord('a')] __ 0:
                continue
            s = ''
            ___ j __ r..(26):
                __ tar[j] > mp[i][j]:
                    s += chr(ord('a')+j)*(tar[j]-mp[i][j])
            tmp = self.helper(mem, mp, s)
            __ tmp != -1:
                res = m..(res, 1+tmp)
        mem[target] = -1 __ res __ float('inf') ____ res
        r.. mem[target]
    
    ___ test(self):
        testCases = [
            [
                ["with", "example", "science"],
                "thehat",
            ],
            [
                ["notice", "possible"],
                "basicbasic",
            ],
        ]
        ___ stickers, target __ testCases:
            print('stickers: %s' % stickers)
            print('target: %s' % target)
            result = self.minStickers(stickers, target)
            print('result: %s' % result)
            print('-='*30+'-')

__ __name__ __ '__main__':
    Solution().test()
