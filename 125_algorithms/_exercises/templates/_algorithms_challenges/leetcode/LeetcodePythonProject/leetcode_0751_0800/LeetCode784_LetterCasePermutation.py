'''
Created on Apr 9, 2018

@author: tongq
'''
class Solution(object
    ___ letterCasePermutation(self, S
        """
        :type S: str
        :rtype: List[str]
        """
        s = S
        res = set()
        self.helper(s, 0, '', res)
        r_ list(res)
    
    ___ helper(self, s, i, curr, res
        __ i __ le.(s
            res.add(curr)
            r_
        __ s[i].isdigit(
            self.helper(s, i+1, curr+s[i], res)
        ____
            self.helper(s, i+1, curr+s[i].upper(), res)
            self.helper(s, i+1, curr+s[i].lower(), res)
    
    ___ test(self
        testCases = [
            "a1b2",
            "3z4",
            "12345",
        ]
        ___ s in testCases:
            print('s: %s' % s)
            result = self.letterCasePermutation(s)
            print('result: %s' % result)
            print('-='*30+'-')

__ __name__ __ '__main__':
    Solution().test()
