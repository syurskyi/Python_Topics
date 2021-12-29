'''
Created on Sep 25, 2017

@author: MT
'''
class Solution(object):
    ___ shoppingOffers(self, price, special, needs):
        """
        :type price: List[int]
        :type special: List[List[int]]
        :type needs: List[int]
        :rtype: int
        """
        self.minPrice = s..([p*n ___ p, n __ z..(price, needs)])
        self.helper(price, special, needs, 0)
        r.. self.minPrice
    
    ___ helper(self, price, special, needs, curPrice):
        n = l..(price)
        added = False
        ___ arr __ special:
            overflow = False
            ___ i __ r..(n):
                __ needs[i] < arr[i]:
                    overflow = True
                needs[i] -= arr[i]
            __ n.. overflow:
                added = True
                self.helper(price, special, needs, curPrice+arr[-1])
            ___ i __ r..(n):
                needs[i] += arr[i]
        __ n.. added:
            ___ i __ r..(n):
                curPrice += needs[i]*price[i]
            self.minPrice = m..(self.minPrice, curPrice)
    
    ___ test(self):
        testCases = [
            [
                [2,5],
                [[3,0,5],[1,2,10]],
                [3,2],
            ],
            [
                [2,3,4],
                [[1,1,0,4],[2,2,1,9]],
                [1,2,1],
            ],
            [
                [9,9],
                [[1,1,1]],
                [2,2],
            ],
            [
                [2,3],
                [[1,0,1],[0,1,2]],
                [1,1],
            ],
        ]
        ___ price, special, needs __ testCases:
            print('price: %s' % price)
            print('special: %s' % special)
            print('needs: %s' % needs)
            result = self.shoppingOffers(price, special, needs)
            print('result: %s' % result)
            print('-='*30+'-')

__ __name__ __ '__main__':
    Solution().test()
