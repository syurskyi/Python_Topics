'''
Created on May 30, 2018

@author: tongq
'''
c_ Solution(object):
    ___ restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        __ l..(s) > 12: r.. []
        res    # list
        helper(res, [], s, 0)
        r.. res
    
    ___ helper(self, res, curr, s, ind):
        __ ind __ l..(s) a.. l..(curr) __ 4:
            res.a..('.'.j..(curr))
        __ ind >= l..(s):
            r..
        ___ i __ r..(ind+1, ind+4):
            sub = s[ind:i]
            __ sub[0] __ '0' a.. l..(sub) > 1:
                break
            __ i..(sub) > 255:
                break
            curr.a..(sub)
            helper(res, curr, s, i)
            curr.pop()
