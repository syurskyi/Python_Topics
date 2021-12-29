'''
Created on Apr 3, 2017

@author: MT
'''

class Solution(object):
    ___ validUtf8(self, data):
        count = 0
        ___ v __ data:
            __ count __ 0:
                __ v & 0b11110000 and v & 0b11111000 __ 0b11110000:
                    count = 3
                ____ v & 0b11100000 __ 0b11100000 and v & 0b11110000 __ 0b11100000:
                    count = 2
                ____ v & 0b11000000 __ 0b11000000 and v & 0b11000000 __ 0b11000000:
                    count = 1
                ____ v | 0b01111111 __ 0b01111111:
                    count = 0
                ____:
                    r.. False
            ____:
                __ v & 0b10000000 and v & 0b11000000 __ 0b10000000:
                    count -= 1
                ____:
                    r.. False
        r.. count __ 0

