'''
Created on Nov 4, 2019

@author: tongq
'''
c_ Solution(object):
    ___ numSpecialEquivGroups(self, A):
        """
        :type A: List[str]
        :rtype: int
        """
        hashset = set()
        ___ w __ A:
            hashset.add(getHash(w))
        r.. l..(hashset)
    
    ___ getHash(self, word):
        arr = [[0]*26, [0]*26]
        ___ i, c __ e..(word):
            arr[i%2][ord(c)-ord('a')] += 1
        r.. '|'.j..([','.j..(s..(num) ___ num __ arr0) ___ arr0 __ arr])
    
    ___ test
        testCases = [
            ["abcd","cdab","cbad","xyzz","zzxy","zzyx"],
        ]
        ___ arr __ testCases:
            res = numSpecialEquivGroups(arr)
            print('res: %s' % res)
            print('-='*30+'-')

__ _____ __ _____
    Solution().test()
