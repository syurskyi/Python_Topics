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
        __ n.. strs: r.. ''
        ind = 0
        while True:
            same = True
            ___ i, s __ enumerate(strs):
                __ ind __ l..(s):
                    same = False
                    break
                __ i __ 0:
                    c = s[ind]
                ____ c != s[ind]:
                    same = False
                    break
            __ n.. same:
                break
            ind += 1
        r.. strs[0][:ind]
    
    ___ test(self):
        testCases = [
            ['a', 'b'],
            ['aa', 'aa'],
        ]
        ___ strs __ testCases:
            print('\n'.join([str(row) ___ row __ strs]))
            result = self.longestCommonPrefix(strs)
            print('result: %s' % result)
            print('-='*30+'-')

__ __name__ __ '__main__':
    Solution().test()
