'''
Created on Apr 6, 2018

@author: tongq
'''
c_ Solution(o..
    ___ minmaxGasDist  stations, K
        """
        :type stations: List[int]
        :type K: int
        :rtype: float
        """
        _______ math
        k = K
        count, n = 0, l..(stations)
        left, right = 0, stations[-1]-stations[0]
        w.... left + 1e-6 < right:
            mid = (left+right)/2.0
            count = 0
            ___ i __ r..(n-1
                count += math.ceil((stations[i+1]-stations[i])/mid)-1
            __ count > k:
                left = mid
            ____:
                right = mid
        r.. right
    
    ___ test
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
        ___ stations, k __ testCases:
            print('stations: %s' % stations)
            print('K: %s' % k)
            result = minmaxGasDist(stations, k)
            print('result: %s' % result)
            print('-='*30+'-')

__ _____ __ _____
    Solution().test()
