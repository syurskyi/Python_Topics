'''
Created on Mar 29, 2017

@author: MT
'''

c_ Solution(o..
    ___ getModifiedArray  length, updates
        result = [0]*length
        ___ update __ updates:
            start = update[0]
            end = update[1]
            increase = update[2]
            result[start] += increase
            __ end < length-1:
                result[end+1] -_ increase
        val = 0
        ___ i __ r..(length
            val += result[i]
            result[i] = val
        r.. result
