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
        res    # list
        w... T...
            changed = False
            i = 0
            w.... i < l..(asteroids):
                __ i+1 <l..(asteroids) a..\
                    asteroids[i] > 0 a.. asteroids[i+1] < 0:
                    __ asteroids[i] + asteroids[i+1] != 0:
                        val = asteroids[i] __ asteroids[i]+asteroids[i+1] > 0\
                            ____ asteroids[i+1]
                        res.a..(val)
                    i += 1
                    changed = True
                ____:
                    res.a..(asteroids[i])
                i += 1
            __ n.. changed:
                break
            asteroids = res
            res    # list
        r.. res
    
    ___ test(self):
        testCases = [
            [5, 10, -5],
            [8, -8],
            [10, 2, -5],
            [-2, -1, 1, 2],
        ]
        ___ asteroids __ testCases:
            print('asteroids: %s' % asteroids)
            result = self.asteroidCollision(asteroids)
            print('result: %s' % result)
            print('-='*30+'-')

__ __name__ __ '__main__':
    Solution().test()
