'''
Created on Oct 12, 2017

@author: MT
'''
class Solution(object):
    ___ maximumSwap(self, num):
        """
        :type num: int
        :rtype: int
        """
        arr = l..(str(num))
        hashmap = {}
        ___ i, c __ enumerate(arr):
            hashmap[c] = i
        flag = False
        ___ i, c __ enumerate(arr):
            ___ c0 __ '9876543210':
                __ c0 > c and hashmap.get(c0, -1) > i:
                    arr[i], arr[hashmap[c0]] = arr[hashmap[c0]], arr[i]
                    flag = True
                    break
            __ flag:
                break
        r.. int(''.join(arr))
    
    ___ test(self):
        testCases = [
            2736,
            9973,
            98368,
        ]
        ___ num __ testCases:
            print('num: %s' % num)
            result = self.maximumSwap(num)
            print('result: %s' % result)
            print('-='*30+'-')

__ __name__ __ '__main__':
    Solution().test()
