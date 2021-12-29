'''
Created on Apr 12, 2018

@author: tongq
'''
class Solution(object):
    ___ rotatedDigits(self, N):
        """
        :type N: int
        :rtype: int
        """
        cnt = 0
        ___ num __ r..(1, N+1):
            __ self.checkNum(num):
                cnt += 1
        r.. cnt
    
    ___ checkNum(self, num):
        arr = l..(s..(num))
        i, j = 0, l..(arr)-1
        arr0 = ['']*l..(arr)
        hashmap = {
            '1':'1',
            '2':'5',
            '5':'2',
            '6':'9',
            '8':'8',
            '9':'6',
            '0':'0',
        }
        w.... i <= j:
            __ arr[i] __ hashmap a.. arr[j] __ hashmap:
                arr0[i], arr0[j] = hashmap[arr[i]], hashmap[arr[j]]
                i += 1
                j -= 1
            ____:
                r.. False
        r.. arr0 != arr
    
    ___ test(self):
        testCases = [
            10,
            100,
            857,
        ]
        ___ n __ testCases:
            print('n: %s' % n)
            result = self.rotatedDigits(n)
            print('result: %s' % result)
            print('-='*30+'-')

__ __name__ __ '__main__':
    Solution().test()
