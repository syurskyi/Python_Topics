'''
Created on Mar 27, 2018

@author: tongq
'''
class Solution(object
    ___ openLock(self, deadends, target
        """
        :type deadends: List[str]
        :type target: str
        :rtype: int
        """
        queue = ['0000']
        level = 0
        visited = set(['0000'])
        deadends = set(deadends)
        __ '0000' __ deadends:
            r_ -1
        w___ queue:
            n = le.(queue)
            ___ _ __ range(n
                s = queue.pop(0)
                __ s __ target:
                    r_ level
                ___ i __ range(4
                    s01 = int(s[i])+1
                    __ s01 >= 10:
                        s01 -= 10
                    s01 = str(s01)
                    s02 = int(s[i])-1
                    __ s02 < 0:
                        s02 += 10
                    s02 = str(s02)
                    s0 = s[:i]+s01+s[i+1:]
                    __ s0 not __ visited and s0 not __ deadends:
                        queue.append(s0)
                        visited.add(s0)
                    s0 = s[:i]+s02+s[i+1:]
                    __ s0 not __ visited and s0 not __ deadends:
                        queue.append(s0)
                        visited.add(s0)
            level += 1
        r_ -1
    
    ___ test(self
        testCases = [
            [
                ["0201","0101","0102","1212","2002"],
                "0202",
            ],
            [
                ["8888"],
                "0009",
            ],
            [
                ["8887","8889","8878","8898","8788","8988","7888","9888"],
                "8888",
            ],
            [
                ["0000"],
                "8888",
            ],
        ]
        ___ deadends, target __ testCases:
            result = self.openLock(deadends, target)
            print('result: %s' % result)
            print('-='*30+'-')

__  -n __ '__main__':
    Solution().test()
