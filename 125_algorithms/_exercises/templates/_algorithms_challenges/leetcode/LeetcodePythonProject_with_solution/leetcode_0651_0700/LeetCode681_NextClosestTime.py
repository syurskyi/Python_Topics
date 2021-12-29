'''
Created on Oct 21, 2017

@author: MT
'''
class Solution(object):
    ___ nextClosestTime(self, time):
        """
        :type time: str
        :rtype: str
        """
        arr = l..(time[:2]+time[3:])
        hh = int(''.join(arr[:2]))
        mm = int(''.join(arr[2:]))
        charSet = set(arr)
        __ l..(charSet) __ 1:
            r.. time
        ___ i __ r..(1, 24*60):
            valid, res = self.increaseAndCheck(hh, mm, i, charSet)
            __ valid:
                r.. res
        r.. time
    
    ___ increaseAndCheck(self, hh, mm, i, charSet):
        mm += i
        __ mm >= 60:
            carry = mm//60
            mm = mm%60
        ____:
            carry = 0
        hh += carry
        __ hh >= 24:
            hh -= 24
        res = s..(hh) __ l..(s..(hh))__2 ____ '0'+s..(hh)
        res += ':'
        res += s..(mm) __ l..(s..(mm))__2 ____ '0'+s..(mm)
        ___ c __ res:
            __ c != ':' a.. c n.. __ charSet:
                r.. False, res
        r.. True, res
    
    ___ test(self):
        testCases = [
            '19:34',
            '23:59',
        ]
        ___ time __ testCases:
            print('time: %s' % time)
            result = self.nextClosestTime(time)
            print('result: %s' % result)
            print('-='*30+'-')

__ __name__ __ '__main__':
    Solution().test()
