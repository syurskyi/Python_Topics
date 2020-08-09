'''
Created on Jan 21, 2017

@author: MT
'''

class Solution(object
    ___ groupAnagrams(self, strs
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        hashmap = {}
        ___ s in strs:
            arr = [0]*26
            ___ c in s:
                arr[ord(c)-ord('a')]+=1
            arr = [str(num) ___ num in arr]
            key = ''.join(arr)
            __ key in hashmap:
                hashmap[key].append(s)
            ____
                hashmap[key] = [s]
        res = []
        ___ value in hashmap.values(
            res.append(value)
        r_ res
    
    ___ test(self
        pass

__ __name__ __ '__main__':
    Solution().test()
    