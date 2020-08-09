'''
Created on Apr 12, 2018

@author: tongq
'''
class Solution(object
    ___ rotatedDigits(self, N
        """
        :type N: int
        :rtype: int
        """
        cnt = 0
        ___ num in range(1, N+1
            __ self.checkNum(num
                cnt += 1
        r_ cnt
    
    ___ checkNum(self, num
        arr = list(str(num))
        i, j = 0, le.(arr)-1
        arr0 = ['']*le.(arr)
        hashmap = {
            '1':'1',
            '2':'5',
            '5':'2',
            '6':'9',
            '8':'8',
            '9':'6',
            '0':'0',
        }
        w___ i <= j:
            __ arr[i] in hashmap and arr[j] in hashmap:
                arr0[i], arr0[j] = hashmap[arr[i]], hashmap[arr[j]]
                i += 1
                j -= 1
            ____
                r_ False
        r_ arr0 != arr
    
    ___ test(self
        testCases = [
            10,
            100,
            857,
        ]
        ___ n in testCases:
            print('n: %s' % n)
            result = self.rotatedDigits(n)
            print('result: %s' % result)
            print('-='*30+'-')

__ __name__ __ '__main__':
    Solution().test()
