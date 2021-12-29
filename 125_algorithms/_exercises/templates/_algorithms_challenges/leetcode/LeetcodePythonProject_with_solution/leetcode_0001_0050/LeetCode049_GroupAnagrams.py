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
        for s in strs:
            arr = [0]*26
            for c in s:
                arr[ord(c)-ord('a')]+=1
            arr = [str(num) for num in arr]
            key = ''.join(arr)
            __ key in hashmap:
                hashmap[key].append(s)
            else:
                hashmap[key] = [s]
        res = []
        for value in hashmap.values():
            res.append(value)
        return res
    
    ___ test(self):
        pass

__ __name__ == '__main__':
    Solution().test()
    