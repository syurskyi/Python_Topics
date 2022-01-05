'''
Created on Jun 5, 2018

@author: tongq
'''
c_ Solution(object):
    ___ multiply  num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        m, n = l..(num1), l..(num2)
        pos = [0]*(m+n)
        ___ i __ r..(m-1, -1, -1):
            ___ j __ r..(n-1, -1, -1):
                val = (o..(num1[i])-o..('0'))*(o..(num2[j])-o..('0'))
                p1 = i+j
                p2 = i+j+1
                sumVal = val+pos[p2]
                pos[p1] += sumVal//10
                pos[p2] = sumVal%10
        res = ''.j..([s..(n) ___ n __ pos]).lstrip('0')
        r.. res __ res ____ '0'
