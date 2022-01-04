'''
Created on Apr 9, 2018

@author: tongq
'''
c_ Solution(object):
    ___ letterCasePermutation(self, S):
        """
        :type S: str
        :rtype: List[str]
        """
        s = S
        res = set()
        helper(s, 0, '', res)
        r.. l..(res)
    
    ___ helper(self, s, i, curr, res):
        __ i __ l..(s):
            res.add(curr)
            r..
        __ s[i].isdigit
            helper(s, i+1, curr+s[i], res)
        ____:
            helper(s, i+1, curr+s[i].u.., res)
            helper(s, i+1, curr+s[i].l.., res)
    
    ___ test
        testCases = [
            "a1b2",
            "3z4",
            "12345",
        ]
        ___ s __ testCases:
            print('s: %s' % s)
            result = letterCasePermutation(s)
            print('result: %s' % result)
            print('-='*30+'-')

__ _____ __ _____
    Solution().test()
