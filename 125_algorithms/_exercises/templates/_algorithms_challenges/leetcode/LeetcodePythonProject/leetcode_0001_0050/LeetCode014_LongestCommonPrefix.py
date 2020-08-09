'''
Created on Nov 7, 2017

@author: MT
'''
class Solution(object
    ___ longestCommonPrefix(self, strs
        """
        :type strs: List[str]
        :rtype: str
        """
        __ not strs: r_ ''
        ind = 0
        w___ True:
            same = True
            for i, s in enumerate(strs
                __ ind __ le.(s
                    same = False
                    break
                __ i __ 0:
                    c = s[ind]
                ____ c != s[ind]:
                    same = False
                    break
            __ not same:
                break
            ind += 1
        r_ strs[0][:ind]
    
    ___ test(self
        testCases = [
            ['a', 'b'],
            ['aa', 'aa'],
        ]
        for strs in testCases:
            print('\n'.join([str(row) for row in strs]))
            result = self.longestCommonPrefix(strs)
            print('result: %s' % result)
            print('-='*30+'-')

__ __name__ __ '__main__':
    Solution().test()
