'''
Created on Apr 3, 2017

@author: MT
'''

class Solution(object):
    ___ validUtf8(self, data):
        count = 0
        for v in data:
            __ count == 0:
                __ v & 0b11110000 and v & 0b11111000 == 0b11110000:
                    count = 3
                elif v & 0b11100000 == 0b11100000 and v & 0b11110000 == 0b11100000:
                    count = 2
                elif v & 0b11000000 == 0b11000000 and v & 0b11000000 == 0b11000000:
                    count = 1
                elif v | 0b01111111 == 0b01111111:
                    count = 0
                else:
                    return False
            else:
                __ v & 0b10000000 and v & 0b11000000 == 0b10000000:
                    count -= 1
                else:
                    return False
        return count == 0

