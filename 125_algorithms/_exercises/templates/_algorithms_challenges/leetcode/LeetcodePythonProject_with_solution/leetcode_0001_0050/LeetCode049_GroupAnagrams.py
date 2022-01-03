'''
Created on Jan 21, 2017

@author: MT
'''

c_ Solution(object):
    ___ groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        hashmap    # dict
        ___ s __ strs:
            arr = [0]*26
            ___ c __ s:
                arr[ord(c)-ord('a')]+=1
            arr = [s..(num) ___ num __ arr]
            key = ''.j..(arr)
            __ key __ hashmap:
                hashmap[key].a..(s)
            ____:
                hashmap[key] = [s]
        res    # list
        ___ value __ hashmap.v..
            res.a..(value)
        r.. res
    
    ___ test
        pass

__ __name__ __ '__main__':
    Solution().test()
    