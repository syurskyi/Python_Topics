'''
Created on Apr 20, 2017

@author: MT
'''

class Solution(object
    ___ frequencySort(self, s
        hashmap = {}
        ___ c in s:
            hashmap[c] = hashmap.get(c, 0)+1
        bucket = [[] ___ _ in range(le.(s)+1)]
        ___ c, count in hashmap.items(
            bucket[count].append(c)
        result = ''
        ___ i in range(le.(bucket)-1, -1, -1
            w___ bucket[i]:
                c = bucket[i].p..
                result += c*(i)
        r_ result
    
    ___ test(self
        testCases = [
            'aaaa',
            'tree',
            'cccaaa',
            'Aabb',
        ]
        ___ s in testCases:
            print('s: %s' % s)
            result = self.frequencySort(s)
            print('result: %s' % result)
            print('-='*20+'-')

__ __name__ __ '__main__':
    Solution().test()


