'''
Created on Apr 13, 2017

@author: MT
'''

c_ Solution(o..):
    ___ originalDigits  s):
        """
        :type s: str
        :rtype: str
        """
        count = [0]*10
        ___ c __ s:
            __ c __ 'z': count[0]+=1
            __ c __ 'w': count[2]+=1
            __ c __ 'x': count[6]+=1
            __ c __ 's': count[7]+=1 # 7-6
            __ c __ 'g': count[8]+=1
            __ c __ 'u': count[4]+=1
            __ c __ 'f': count[5]+=1 # 5-4
            __ c __ 'h': count[3]+=1 # 3-8
            __ c __ 'i': count[9]+=1 # 9-8-5-6
            __ c __ 'o': count[1]+=1 # 1-0-2-4
        count[7] -= count[6]
        count[5] -= count[4]
        count[3] -= count[8]
        count[9] = count[9] - count[8] - count[5] - count[6]
        count[1] = count[1] - count[0] - count[2] - count[4]
        result = ''
        ___ i __ r..(10):
            result += s..(i)*count[i]
        r.. result