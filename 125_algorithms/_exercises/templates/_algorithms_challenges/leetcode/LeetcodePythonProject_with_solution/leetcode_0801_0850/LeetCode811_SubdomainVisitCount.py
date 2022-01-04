'''
Created on Apr 25, 2018

@author: tongq
'''
c_ Solution(object):
    ___ subdomainVisits(self, cpdomains):
        """
        :type cpdomains: List[str]
        :rtype: List[str]
        """
        hashmap    # dict
        ___ s __ cpdomains:
            cnt, s = s.s..(' ')
            cnt = i..(cnt)
            arr = s.s..('.')[::-1]
            ___ i __ r..(1, l..(arr)+1):
                s0 = '.'.j..(arr[:i][::-1])
                hashmap[s0] = hashmap.get(s0, 0)+cnt
        res    # list
        ___ s, freq __ hashmap.i..:
            res.a..(s..(freq) + ' ' + s)
        r.. res
    
    ___ test
        testCases = [
            ["9001 discuss.leetcode.com"],
            ["900 google.mail.com", "50 yahoo.com", "1 intel.mail.com", "5 wiki.org"],
        ]
        ___ cpdomains __ testCases:
            result = subdomainVisits(cpdomains)
            print('result: %s' % result)
            print('-='*30+'-')

__ _____ __ _____
    Solution().test()
