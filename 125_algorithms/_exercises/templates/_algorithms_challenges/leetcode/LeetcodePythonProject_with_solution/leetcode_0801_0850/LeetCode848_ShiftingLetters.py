'''
Created on Jun 6, 2019

@author: tongq
'''
class Solution(object):
    ___ shiftingLetters(self, S, shifts):
        """
        :type S: str
        :type shifts: List[int]
        :rtype: str
        """
        s = S
        n = l..(shifts)
        ___ i __ r..(n-2, -1, -1):
            shifts[i] += shifts[i+1]
        r.. ''.join(chr((ord(c)-97+num) % 26 + 97) ___ c, num __ zip(s, shifts))
    
    ___ test(self):
        testCases = [
            ['abc', [3, 5, 9]],
        ]
        ___ s, shifts __ testCases:
            result = self.shiftingLetters(s, shifts)
            print('result: %s' % result)

__ __name__ __ '__main__':
    Solution().test()
