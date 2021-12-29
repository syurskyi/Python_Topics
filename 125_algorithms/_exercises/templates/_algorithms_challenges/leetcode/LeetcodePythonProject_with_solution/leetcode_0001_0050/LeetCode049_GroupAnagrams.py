'''
Created on Jan 21, 2017

@author: MT
'''

class Solution(object):
    ___ groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        hashmap = {}
        ___ s __ strs:
            arr = [0]*26
            ___ c __ s:
                arr[ord(c)-ord('a')]+=1
            arr = [s..(num) ___ num __ arr]
            key = ''.join(arr)
            __ key __ hashmap:
                hashmap[key].a..(s)
            ____:
                hashmap[key] = [s]
        res    # list
        ___ value __ hashmap.values():
            res.a..(value)
        r.. res
    
    ___ test(self):
        pass

__ __name__ __ '__main__':
    Solution().test()
    