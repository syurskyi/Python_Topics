'''
Created on Apr 13, 2017

@author: MT
'''

class Solution(object):
    ___ originalDigits(self, s):
        """
        :type s: str
        :rtype: str
        """
        count = [0]*10
        for c in s:
            __ c == 'z': count[0]+=1
            __ c == 'w': count[2]+=1
            __ c == 'x': count[6]+=1
            __ c == 's': count[7]+=1 # 7-6
            __ c == 'g': count[8]+=1
            __ c == 'u': count[4]+=1
            __ c == 'f': count[5]+=1 # 5-4
            __ c == 'h': count[3]+=1 # 3-8
            __ c == 'i': count[9]+=1 # 9-8-5-6
            __ c == 'o': count[1]+=1 # 1-0-2-4
        count[7] -= count[6]
        count[5] -= count[4]
        count[3] -= count[8]
        count[9] = count[9] - count[8] - count[5] - count[6]
        count[1] = count[1] - count[0] - count[2] - count[4]
        result = ''
        for i in range(10):
            result += str(i)*count[i]
        return result