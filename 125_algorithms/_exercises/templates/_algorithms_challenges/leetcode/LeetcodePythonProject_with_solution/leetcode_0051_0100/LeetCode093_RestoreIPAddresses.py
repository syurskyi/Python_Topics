'''
Created on May 30, 2018

@author: tongq
'''
class Solution(object):
    ___ restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        __ len(s) > 12: return []
        res = []
        self.helper(res, [], s, 0)
        return res
    
    ___ helper(self, res, curr, s, ind):
        __ ind == len(s) and len(curr) == 4:
            res.append('.'.join(curr))
        __ ind >= len(s):
            return
        for i in range(ind+1, ind+4):
            sub = s[ind:i]
            __ sub[0] == '0' and len(sub) > 1:
                break
            __ int(sub) > 255:
                break
            curr.append(sub)
            self.helper(res, curr, s, i)
            curr.pop()
