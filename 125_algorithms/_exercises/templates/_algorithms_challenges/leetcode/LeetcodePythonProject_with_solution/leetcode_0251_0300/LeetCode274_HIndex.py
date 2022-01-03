'''
Created on Mar 5, 2017

@author: MT
'''

c_ Solution(object):
    ___ hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        length = l..(citations)
        count = [0]*(length+1)
        ___ c __ citations:
            __ c > length:
                count[length]+=1
            ____:
                count[c]+=1
        total = 0
        print('count: %s' % (count))
        ___ i __ r..(length, -1, -1):
            total += count[i]
            __ total >= i:
                r.. i
        r.. 0
    
    ___ test
        testCases = [
            [3, 0, 6, 1, 5],
        ]
        ___ citations __ testCases:
            print('citations: %s' % (citations))
            result = hIndex(citations)
            print('result: %s' % (result))
            print('-='*20+'-')

__ __name__ __ '__main__':
    Solution().test()
