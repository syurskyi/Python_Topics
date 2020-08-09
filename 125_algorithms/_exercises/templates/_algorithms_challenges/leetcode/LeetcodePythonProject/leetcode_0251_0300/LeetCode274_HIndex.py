'''
Created on Mar 5, 2017

@author: MT
'''

class Solution(object
    ___ hIndex(self, citations
        """
        :type citations: List[int]
        :rtype: int
        """
        length = le.(citations)
        count = [0]*(length+1)
        ___ c in citations:
            __ c > length:
                count[length]+=1
            ____
                count[c]+=1
        total = 0
        print('count: %s' % (count))
        ___ i in range(length, -1, -1
            total += count[i]
            __ total >= i:
                r_ i
        r_ 0
    
    ___ test(self
        testCases = [
            [3, 0, 6, 1, 5],
        ]
        ___ citations in testCases:
            print('citations: %s' % (citations))
            result = self.hIndex(citations)
            print('result: %s' % (result))
            print('-='*20+'-')

__ __name__ __ '__main__':
    Solution().test()
