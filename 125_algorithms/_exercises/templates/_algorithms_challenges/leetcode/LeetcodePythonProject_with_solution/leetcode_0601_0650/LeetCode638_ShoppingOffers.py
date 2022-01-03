'''
Created on Sep 25, 2017

@author: MT
'''
c_ Solution(object):
    ___ shoppingOffers(self, price, special, needs):
        """
        :type price: List[int]
        :type special: List[List[int]]
        :type needs: List[int]
        :rtype: int
        """
        minPrice = s..([p*n ___ p, n __ z..(price, needs)])
        helper(price, special, needs, 0)
        r.. minPrice
    
    ___ helper(self, price, special, needs, curPrice):
        n = l..(price)
        added = F..
        ___ arr __ special:
            overflow = F..
            ___ i __ r..(n):
                __ needs[i] < arr[i]:
                    overflow = T..
                needs[i] -= arr[i]
            __ n.. overflow:
                added = T..
                helper(price, special, needs, curPrice+arr[-1])
            ___ i __ r..(n):
                needs[i] += arr[i]
        __ n.. added:
            ___ i __ r..(n):
                curPrice += needs[i]*price[i]
            minPrice = m..(minPrice, curPrice)
    
    ___ test
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
            result = shoppingOffers(price, special, needs)
            print('result: %s' % result)
            print('-='*30+'-')

__ __name__ __ '__main__':
    Solution().test()
