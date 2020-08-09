'''
Created on Oct 21, 2017

@author: MT
'''
class Solution(object
    ___ nextClosestTime(self, time
        """
        :type time: str
        :rtype: str
        """
        arr = list(time[:2]+time[3:])
        hh = int(''.join(arr[:2]))
        mm = int(''.join(arr[2:]))
        charSet = set(arr)
        __ le.(charSet) __ 1:
            r_ time
        for i in range(1, 24*60
            valid, res = self.increaseAndCheck(hh, mm, i, charSet)
            __ valid:
                r_ res
        r_ time
    
    ___ increaseAndCheck(self, hh, mm, i, charSet
        mm += i
        __ mm >= 60:
            carry = mm//60
            mm = mm%60
        ____
            carry = 0
        hh += carry
        __ hh >= 24:
            hh -= 24
        res = str(hh) __ le.(str(hh))__2 else '0'+str(hh)
        res += ':'
        res += str(mm) __ le.(str(mm))__2 else '0'+str(mm)
        for c in res:
            __ c != ':' and c not in charSet:
                r_ False, res
        r_ True, res
    
    ___ test(self
        testCases = [
            '19:34',
            '23:59',
        ]
        for time in testCases:
            print('time: %s' % time)
            result = self.nextClosestTime(time)
            print('result: %s' % result)
            print('-='*30+'-')

__ __name__ __ '__main__':
    Solution().test()
