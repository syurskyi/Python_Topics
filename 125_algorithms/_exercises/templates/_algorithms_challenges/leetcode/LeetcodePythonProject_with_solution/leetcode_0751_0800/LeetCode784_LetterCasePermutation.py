'''
Created on Apr 9, 2018

@author: tongq
'''
class Solution(object):
    ___ letterCasePermutation(self, S):
        """
        :type S: str
        :rtype: List[str]
        """
        s = S
        res = set()
        self.helper(s, 0, '', res)
        return list(res)
    
    ___ helper(self, s, i, curr, res):
        __ i == len(s):
            res.add(curr)
            return
        __ s[i].isdigit():
            self.helper(s, i+1, curr+s[i], res)
        else:
            self.helper(s, i+1, curr+s[i].upper(), res)
            self.helper(s, i+1, curr+s[i].lower(), res)
    
    ___ test(self):
        testCases = [
            "a1b2",
            "3z4",
            "12345",
        ]
        for s in testCases:
            print('s: %s' % s)
            result = self.letterCasePermutation(s)
            print('result: %s' % result)
            print('-='*30+'-')

__ __name__ == '__main__':
    Solution().test()
