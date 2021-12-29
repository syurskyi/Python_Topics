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
        n = len(stickers)
        mp = [[0]*26 for _ in range(n)]
        for i in range(n):
            for c in stickers[i]:
                mp[i][ord(c)-ord('a')] += 1
        mem = {}
        mem[''] = 0
        return self.helper(mem, mp, target)
    
    ___ helper(self, mem, mp, target):
        __ target in mem:
            return mem[target]
        n = len(mp)
        tar = [0]*26
        for c in target:
            tar[ord(c)-ord('a')] += 1
        res = float('inf')
        for i in range(n):
            __ mp[i][ord(target[0])-ord('a')] == 0:
                continue
            s = ''
            for j in range(26):
                __ tar[j] > mp[i][j]:
                    s += chr(ord('a')+j)*(tar[j]-mp[i][j])
            tmp = self.helper(mem, mp, s)
            __ tmp != -1:
                res = min(res, 1+tmp)
        mem[target] = -1 __ res == float('inf') else res
        return mem[target]
    
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
        for stickers, target in testCases:
            print('stickers: %s' % stickers)
            print('target: %s' % target)
            result = self.minStickers(stickers, target)
            print('result: %s' % result)
            print('-='*30+'-')

__ __name__ == '__main__':
    Solution().test()
