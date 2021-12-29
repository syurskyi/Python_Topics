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
        for a in accounts:
            for i in range(1, len(a)):
                parents[a[i]] = a[i]
                owner[a[i]] = a[0]
        for a in accounts:
            p = self.find(a[1], parents)
            for i in range(2, len(a)):
                parents[self.find(a[i], parents)] = p
        for a in accounts:
            p = self.find(a[1], parents)
            __ p not in unions:
                unions[p] = set()
            for i in range(1, len(a)):
                unions[p].add(a[i])
        res = []
        for p in unions:
            emails = sorted(list(unions[p]))
            emails.insert(0, owner[p])
            res.append(emails)
        return res
    
    ___ find(self, s, hashmap):
        return s __ hashmap[s] == s else self.find(hashmap[s], hashmap)
    
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
        for accounts in testCases:
            print('accounts:')
            print('\n'.join([str(row) for row in accounts]))
            result = self.accountsMerge(accounts)
            print('result:')
            print('\n'.join([str(row) for row in result]))
            print('-='*30+'-')

__ __name__ == '__main__':
    Solution().test()
