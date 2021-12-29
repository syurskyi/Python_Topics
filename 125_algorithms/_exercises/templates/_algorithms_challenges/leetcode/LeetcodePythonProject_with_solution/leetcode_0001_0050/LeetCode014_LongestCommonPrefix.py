'''
Created on Nov 7, 2017

@author: MT
'''
class Solution(object):
    ___ longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        __ not strs: return ''
        ind = 0
        while True:
            same = True
            for i, s in enumerate(strs):
                __ ind == len(s):
                    same = False
                    break
                __ i == 0:
                    c = s[ind]
                elif c != s[ind]:
                    same = False
                    break
            __ not same:
                break
            ind += 1
        return strs[0][:ind]
    
    ___ test(self):
        testCases = [
            ['a', 'b'],
            ['aa', 'aa'],
        ]
        for strs in testCases:
            print('\n'.join([str(row) for row in strs]))
            result = self.longestCommonPrefix(strs)
            print('result: %s' % result)
            print('-='*30+'-')

__ __name__ == '__main__':
    Solution().test()
