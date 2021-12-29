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
        arr = list(time[:2]+time[3:])
        hh = int(''.join(arr[:2]))
        mm = int(''.join(arr[2:]))
        charSet = set(arr)
        __ len(charSet) == 1:
            return time
        for i in range(1, 24*60):
            valid, res = self.increaseAndCheck(hh, mm, i, charSet)
            __ valid:
                return res
        return time
    
    ___ increaseAndCheck(self, hh, mm, i, charSet):
        mm += i
        __ mm >= 60:
            carry = mm//60
            mm = mm%60
        else:
            carry = 0
        hh += carry
        __ hh >= 24:
            hh -= 24
        res = str(hh) __ len(str(hh))==2 else '0'+str(hh)
        res += ':'
        res += str(mm) __ len(str(mm))==2 else '0'+str(mm)
        for c in res:
            __ c != ':' and c not in charSet:
                return False, res
        return True, res
    
    ___ test(self):
        testCases = [
            '19:34',
            '23:59',
        ]
        for time in testCases:
            print('time: %s' % time)
            result = self.nextClosestTime(time)
            print('result: %s' % result)
            print('-='*30+'-')

__ __name__ == '__main__':
    Solution().test()
