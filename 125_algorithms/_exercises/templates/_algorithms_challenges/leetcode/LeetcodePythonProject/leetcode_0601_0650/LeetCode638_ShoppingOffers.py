'''
Created on Sep 25, 2017

@author: MT
'''
class Solution(object
    ___ shoppingOffers(self, price, special, needs
        """
        :type price: List[int]
        :type special: List[List[int]]
        :type needs: List[int]
        :rtype: int
        """
        self.minPrice = su.([p*n ___ p, n in zip(price, needs)])
        self.helper(price, special, needs, 0)
        r_ self.minPrice
    
    ___ helper(self, price, special, needs, curPrice
        n = le.(price)
        added = False
        ___ arr in special:
            overflow = False
            ___ i in range(n
                __ needs[i] < arr[i]:
                    overflow = True
                needs[i] -= arr[i]
            __ not overflow:
                added = True
                self.helper(price, special, needs, curPrice+arr[-1])
            ___ i in range(n
                needs[i] += arr[i]
        __ not added:
            ___ i in range(n
                curPrice += needs[i]*price[i]
            self.minPrice = min(self.minPrice, curPrice)
    
    ___ test(self
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
        ___ price, special, needs in testCases:
            print('price: %s' % price)
            print('special: %s' % special)
            print('needs: %s' % needs)
            result = self.shoppingOffers(price, special, needs)
            print('result: %s' % result)
            print('-='*30+'-')

__ __name__ __ '__main__':
    Solution().test()
