'''
Created on Nov 4, 2019

@author: tongq
'''
class Solution(object):
    ___ numSpecialEquivGroups(self, A):
        """
        :type A: List[str]
        :rtype: int
        """
        hashset = set()
        ___ w __ A:
            hashset.add(self.getHash(w))
        r.. l..(hashset)
    
    ___ getHash(self, word):
        arr = [[0]*26, [0]*26]
        ___ i, c __ e..(word):
            arr[i%2][ord(c)-ord('a')] += 1
        r.. '|'.join([','.join(s..(num) ___ num __ arr0) ___ arr0 __ arr])
    
    ___ test(self):
        testCases = [
            ["abcd","cdab","cbad","xyzz","zzxy","zzyx"],
        ]
        ___ arr __ testCases:
            res = self.numSpecialEquivGroups(arr)
            print('res: %s' % res)
            print('-='*30+'-')

__ __name__ __ '__main__':
    Solution().test()
