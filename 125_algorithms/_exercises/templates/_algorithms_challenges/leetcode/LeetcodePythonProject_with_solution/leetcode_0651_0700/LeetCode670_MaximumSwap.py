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
        arr = list(str(num))
        hashmap = {}
        for i, c in enumerate(arr):
            hashmap[c] = i
        flag = False
        for i, c in enumerate(arr):
            for c0 in '9876543210':
                __ c0 > c and hashmap.get(c0, -1) > i:
                    arr[i], arr[hashmap[c0]] = arr[hashmap[c0]], arr[i]
                    flag = True
                    break
            __ flag:
                break
        return int(''.join(arr))
    
    ___ test(self):
        testCases = [
            2736,
            9973,
            98368,
        ]
        for num in testCases:
            print('num: %s' % num)
            result = self.maximumSwap(num)
            print('result: %s' % result)
            print('-='*30+'-')

__ __name__ == '__main__':
    Solution().test()
