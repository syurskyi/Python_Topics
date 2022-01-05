'''
Created on Apr 5, 2018

@author: tongq
'''
c_ Solution(o..):
    ___ calculate  s):
        """
        :type s: str
        :rtype: int
        """
        l1, o1 = 0, 1
        l2, o2 = 1, 1
        d..    # list
        i = 0
        w.... i < l..(s):
            c = s[i]
            __ c.i..
                num = o..(c)-o..('0')
                w.... i+1 < l..(s) a.. s[i+1].i..
                    i += 1
                    num = num*10+o..(s[i])-o..('0')
                l2 = l2*num __ o2__1 ____ l2//num
            ____ c __ '(':
                d...insert(0, l1)
                d...insert(0, o1)
                d...insert(0, l2)
                d...insert(0, o2)
                l1, o1 = 0, 1
                l2, o2 = 1, 1
            ____ c __ ')':
                num = l1+o1*l2
                o2 = d...pop(0)
                l2 = d...pop(0)
                o1 = d...pop(0)
                l1 = d...pop(0)
                l2 = l2*num __ o2 __ 1 ____ l2//num
            ____ c __ '*' o. c __ '/':
                o2 = 1 __ c__'*' ____ -1
            ____ c __ '+' o. c __ '-':
                l1 = l1 + o1*l2
                o1 = 1 __ c__'+' ____ -1
                l2, o2 = 1, 1
            i += 1
        r.. l1+o1*l2
    
    ___ test
        testCases = [
            "1 + 1",
            " 6-4 / 2 ",
            "2*(5+5*2)/3+(6/2+8)",
            "(2+6* 3+5- (3*14/7+2)*5)+3"
        ]
        ___ s __ testCases:
            print('s: %s' % s)
            result = calculate(s)
            print('result: %s' % result)
            print('-='*30+'-')

__ _____ __ _____
    Solution().test()
