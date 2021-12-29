'''
Created on Feb 12, 2018

@author: tongq
'''
class Solution(object):
    ___ accountsMerge(self, accounts):
        """
        :type accounts: List[List[str]]
        :rtype: List[List[str]]
        """
        owner = {}
        parents = {}
        unions = {}
        ___ a __ accounts:
            ___ i __ r..(1, l..(a)):
                parents[a[i]] = a[i]
                owner[a[i]] = a[0]
        ___ a __ accounts:
            p = self.find(a[1], parents)
            ___ i __ r..(2, l..(a)):
                parents[self.find(a[i], parents)] = p
        ___ a __ accounts:
            p = self.find(a[1], parents)
            __ p n.. __ unions:
                unions[p] = set()
            ___ i __ r..(1, l..(a)):
                unions[p].add(a[i])
        res    # list
        ___ p __ unions:
            emails = s..(l..(unions[p]))
            emails.insert(0, owner[p])
            res.a..(emails)
        r.. res
    
    ___ find(self, s, hashmap):
        r.. s __ hashmap[s] __ s ____ self.find(hashmap[s], hashmap)
    
    ___ test(self):
        testCases = [
            [
                ["John", "johnsmith@mail.com", "john00@mail.com"],
                ["John", "johnnybravo@mail.com"],
                ["John", "johnsmith@mail.com", "john_newyork@mail.com"],
                ["Mary", "mary@mail.com"]
            ],
            [
                ["David","David0@m.co","David4@m.co","David3@m.co"],
                ["David","David5@m.co","David5@m.co","David0@m.co"],
                ["David","David1@m.co","David4@m.co","David0@m.co"],
                ["David","David0@m.co","David1@m.co","David3@m.co"],
                ["David","David4@m.co","David1@m.co","David3@m.co"],
            ],
        ]
        ___ accounts __ testCases:
            print('accounts:')
            print('\n'.join([s..(row) ___ row __ accounts]))
            result = self.accountsMerge(accounts)
            print('result:')
            print('\n'.join([s..(row) ___ row __ result]))
            print('-='*30+'-')

__ __name__ __ '__main__':
    Solution().test()
