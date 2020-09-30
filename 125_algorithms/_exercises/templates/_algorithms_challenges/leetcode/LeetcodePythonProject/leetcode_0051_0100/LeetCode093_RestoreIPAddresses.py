'''
Created on May 30, 2018

@author: tongq
'''
class Solution(object
    ___ restoreIpAddresses(self, s
        """
        :type s: str
        :rtype: List[str]
        """
        __ le.(s) > 12: r_   # list
        res =   # list
        self.helper(res,   # list, s, 0)
        r_ res
    
    ___ helper(self, res, curr, s, ind
        __ ind __ le.(s) and le.(curr) __ 4:
            res.append('.'.join(curr))
        __ ind >= le.(s
            r_
        ___ i __ range(ind+1, ind+4
            sub = s[ind:i]
            __ sub[0] __ '0' and le.(sub) > 1:
                break
            __ int(sub) > 255:
                break
            curr.append(sub)
            self.helper(res, curr, s, i)
            curr.p..
