'''
Created on Apr 5, 2018

@author: tongq
'''
c_ Solution(object):
    ___ calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        l1, o1 = 0, 1
        l2, o2 = 1, 1
        deque    # list
        i = 0
        w.... i < l..(s):
            c = s[i]
            __ c.isdigit():
                num = ord(c)-ord('0')
                w.... i+1 < l..(s) a.. s[i+1].isdigit():
                    i += 1
                    num = num*10+ord(s[i])-ord('0')
                l2 = l2*num __ o2__1 ____ l2//num
            ____ c __ '(':
                deque.insert(0, l1)
                deque.insert(0, o1)
                deque.insert(0, l2)
                deque.insert(0, o2)
                l1, o1 = 0, 1
                l2, o2 = 1, 1
            ____ c __ ')':
                num = l1+o1*l2
                o2 = deque.pop(0)
                l2 = deque.pop(0)
                o1 = deque.pop(0)
                l1 = deque.pop(0)
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

__ __name__ __ '__main__':
    Solution().test()
