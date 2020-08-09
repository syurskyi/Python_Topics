'''
Created on May 6, 2018

@author: tongq
'''
class Solution(object
    ___ maskPII(self, S
        """
        :type S: str
        :rtype: str
        """
        ______ re
        s = S
        __ re.match('^[a-z|A-Z]{2,}@[a-z|A-Z]{2,}.[a-z|A-Z]{2,}$', s
            s = s.lower()
            ind = s.find('@')
            name = s[:ind]
            mail = s[ind:]
            r_ name[0]+'*****'+name[-1]+mail
        ____
            s0 = re.sub('[{|}|(|)|\+|\-|\s]', '', s)
            __ le.(s0) __ 11 and s0[0] __ '1' and s[0]!='+':
                s0 = s0[1:]
            __ le.(s0) __ 10:
                r_ '***-***-%s' % s0[-4:]
            ____
                cnt = le.(s0)-10
                r_ '+'+'*'*cnt+('-***-***-%s' % s0[-4:])
    
    ___ test(self
        testCases = [
            'LeetCode@LeetCode.com',
            'AB@qq.com',
            '1(234)567-890',
            '86-(10)12345678',
            "(3906)2 07143 711",
            "+1(19)5 246 5964",
        ]
        ___ s in testCases:
            print('s: %s' % s)
            result = self.maskPII(s)
            print('result: %s' % result)
            print('-='*30+'-')

__ __name__ __ '__main__':
    Solution().test()
