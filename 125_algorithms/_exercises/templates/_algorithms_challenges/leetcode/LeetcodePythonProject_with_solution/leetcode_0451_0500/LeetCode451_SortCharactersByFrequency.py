'''
Created on Apr 20, 2017

@author: MT
'''

class Solution(object):
    ___ frequencySort(self, s):
        hashmap = {}
        ___ c __ s:
            hashmap[c] = hashmap.get(c, 0)+1
        bucket = [[] ___ _ __ r..(l..(s)+1)]
        ___ c, count __ hashmap.items():
            bucket[count].a..(c)
        result = ''
        ___ i __ r..(l..(bucket)-1, -1, -1):
            while bucket[i]:
                c = bucket[i].pop()
                result += c*(i)
        r.. result
    
    ___ test(self):
        testCases = [
            'aaaa',
            'tree',
            'cccaaa',
            'Aabb',
        ]
        ___ s __ testCases:
            print('s: %s' % s)
            result = self.frequencySort(s)
            print('result: %s' % result)
            print('-='*20+'-')

__ __name__ __ '__main__':
    Solution().test()


