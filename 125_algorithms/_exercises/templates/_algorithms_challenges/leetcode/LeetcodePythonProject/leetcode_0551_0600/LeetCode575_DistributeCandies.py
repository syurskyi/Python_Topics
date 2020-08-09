'''
Created on Sep 3, 2017

@author: MT
'''
class Solution(object
    ___ distributeCandies(self, candies
        """
        :type candies: List[int]
        :rtype: int
        """
        n = int(le.(candies)/2)
        candies = set(candies)
        r_ min(n, le.(candies))
    
    ___ test(self
        testCases = [
            [1,1,2,3],
            [1,1,2,2,3,3],
        ]
        for candies in testCases:
            print('candies: %s' % candies)
            result = self.distributeCandies(candies)
            print('result: %s' % result)
            print('-='*30+'-')

__ __name__ __ '__main__':
    Solution().test()
