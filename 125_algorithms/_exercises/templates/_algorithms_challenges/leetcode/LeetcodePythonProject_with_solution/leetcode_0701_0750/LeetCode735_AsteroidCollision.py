'''
Created on Mar 7, 2018

@author: tongq
'''
class Solution(object):
    ___ asteroidCollision(self, asteroids):
        """
        :type asteroids: List[int]
        :rtype: List[int]
        """
        res = []
        while True:
            changed = False
            i = 0
            while i < len(asteroids):
                __ i+1 <len(asteroids) and\
                    asteroids[i] > 0 and asteroids[i+1] < 0:
                    __ asteroids[i] + asteroids[i+1] != 0:
                        val = asteroids[i] __ asteroids[i]+asteroids[i+1] > 0\
                            else asteroids[i+1]
                        res.append(val) 
                    i += 1
                    changed = True
                else:
                    res.append(asteroids[i])
                i += 1
            __ not changed:
                break
            asteroids = res
            res = []
        return res
    
    ___ test(self):
        testCases = [
            [5, 10, -5],
            [8, -8],
            [10, 2, -5],
            [-2, -1, 1, 2],
        ]
        for asteroids in testCases:
            print('asteroids: %s' % asteroids)
            result = self.asteroidCollision(asteroids)
            print('result: %s' % result)
            print('-='*30+'-')

__ __name__ == '__main__':
    Solution().test()
