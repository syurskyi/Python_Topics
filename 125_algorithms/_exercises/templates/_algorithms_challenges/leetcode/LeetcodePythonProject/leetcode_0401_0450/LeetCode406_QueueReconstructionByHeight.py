'''
Created on Apr 10, 2017

@author: MT
'''

class Solution(object
    ___ reconstructQueue(self, people
        res = []
        people.sort(key=lambda x: (-x[0], x[1]))
        ___ p in people:
            res.insert(p[1], p)
        r_ res
        
    ___ test(self
        testCases = [
            [[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]],
        ]
        ___ people in testCases:
            print('people: %s' % people)
            result = self.reconstructQueue(people)
            print('result: %s' % result)
            print('-='*30+'-')

__ __name__ __ '__main__':
    Solution().test()
