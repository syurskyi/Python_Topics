'''
Created on Apr 6, 2018

@author: tongq
'''
class Solution(object
    ___ minmaxGasDist(self, stations, K
        """
        :type stations: List[int]
        :type K: int
        :rtype: float
        """
        ______ ma__
        k = K
        count, n = 0, le.(stations)
        left, right = 0, stations[-1]-stations[0]
        w___ left + 1e-6 < right:
            mid = (left+right)/2.0
            count = 0
            ___ i in range(n-1
                count += ma__.ceil((stations[i+1]-stations[i])/mid)-1
            __ count > k:
                left = mid
            ____
                right = mid
        r_ right
    
    ___ test(self
        testCases = [
            [
                [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
                9,
            ],
            [
                [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
                7,
            ],
        ]
        ___ stations, k in testCases:
            print('stations: %s' % stations)
            print('K: %s' % k)
            result = self.minmaxGasDist(stations, k)
            print('result: %s' % result)
            print('-='*30+'-')

__ __name__ __ '__main__':
    Solution().test()
