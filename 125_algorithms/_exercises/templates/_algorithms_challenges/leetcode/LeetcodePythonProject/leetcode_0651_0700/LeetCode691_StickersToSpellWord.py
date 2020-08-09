'''
Created on Oct 24, 2017

@author: MT
'''
class Solution(object
    ___ minStickers(self, stickers, target
        """
        :type stickers: List[str]
        :type target: str
        :rtype: int
        """
        n = le.(stickers)
        mp = [[0]*26 ___ _ in range(n)]
        ___ i in range(n
            ___ c in stickers[i]:
                mp[i][ord(c)-ord('a')] += 1
        mem = {}
        mem[''] = 0
        r_ self.helper(mem, mp, target)
    
    ___ helper(self, mem, mp, target
        __ target in mem:
            r_ mem[target]
        n = le.(mp)
        tar = [0]*26
        ___ c in target:
            tar[ord(c)-ord('a')] += 1
        res = float('inf')
        ___ i in range(n
            __ mp[i][ord(target[0])-ord('a')] __ 0:
                continue
            s = ''
            ___ j in range(26
                __ tar[j] > mp[i][j]:
                    s += chr(ord('a')+j)*(tar[j]-mp[i][j])
            tmp = self.helper(mem, mp, s)
            __ tmp != -1:
                res = min(res, 1+tmp)
        mem[target] = -1 __ res __ float('inf') else res
        r_ mem[target]
    
    ___ test(self
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
        ___ stickers, target in testCases:
            print('stickers: %s' % stickers)
            print('target: %s' % target)
            result = self.minStickers(stickers, target)
            print('result: %s' % result)
            print('-='*30+'-')

__ __name__ __ '__main__':
    Solution().test()
