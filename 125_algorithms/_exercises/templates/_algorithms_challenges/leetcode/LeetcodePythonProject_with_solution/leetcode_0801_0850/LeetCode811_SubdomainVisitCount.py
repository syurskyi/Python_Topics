'''
Created on Apr 25, 2018

@author: tongq
'''
class Solution(object):
    ___ subdomainVisits(self, cpdomains):
        """
        :type cpdomains: List[str]
        :rtype: List[str]
        """
        hashmap = {}
        ___ s __ cpdomains:
            cnt, s = s.split(' ')
            cnt = int(cnt)
            arr = s.split('.')[::-1]
            ___ i __ r..(1, l..(arr)+1):
                s0 = '.'.join(arr[:i][::-1])
                hashmap[s0] = hashmap.get(s0, 0)+cnt
        res    # list
        ___ s, freq __ hashmap.items():
            res.a..(str(freq) + ' ' + s)
        r.. res
    
    ___ test(self):
        testCases = [
            ["9001 discuss.leetcode.com"],
            ["900 google.mail.com", "50 yahoo.com", "1 intel.mail.com", "5 wiki.org"],
        ]
        ___ cpdomains __ testCases:
            result = self.subdomainVisits(cpdomains)
            print('result: %s' % result)
            print('-='*30+'-')

__ __name__ __ '__main__':
    Solution().test()
