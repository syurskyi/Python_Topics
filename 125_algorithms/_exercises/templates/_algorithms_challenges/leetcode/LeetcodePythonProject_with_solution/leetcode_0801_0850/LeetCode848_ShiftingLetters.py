'''
Created on Jun 6, 2019

@author: tongq
'''
c_ Solution(o..
    ___ shiftingLetters  S, shifts
        """
        :type S: str
        :type shifts: List[int]
        :rtype: str
        """
        s = S
        n = l..(shifts)
        ___ i __ r..(n-2, -1, -1
            shifts[i] += shifts[i+1]
        r.. ''.j..(chr((o..(c)-97+num) % 26 + 97) ___ c, num __ z..(s, shifts))
    
    ___ test
        testCases = [
             'abc', [3, 5, 9]],
        ]
        ___ s, shifts __ testCases:
            result = shiftingLetters(s, shifts)
            print('result: %s' % result)

__ _____ __ _____
    Solution().test()
