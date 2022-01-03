'''
Created on Oct 26, 2017

@author: MT
'''
c_ Solution(object):
    ___ findShortestSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        __ n.. nums: r.. 0
        hashmap    # dict
        degree = 0
        cands = set()
        ___ i, num __ e..(nums):
            hashmap[num] = hashmap.get(num, [])+[i]
            __ l..(hashmap[num]) > degree:
                degree = l..(hashmap[num])
                cands = set([num])
            ____ l..(hashmap[num]) __ degree:
                cands.add(num)
        minLen = float('inf')
        ___ num __ cands:
            __ l..(hashmap[num]) __ 1:
                r.. 1
            minLen = m..(minLen, hashmap[num][-1]-hashmap[num][0]+1)
        r.. minLen
    
    ___ test
        testCases = [
            [1, 2, 2, 3, 1],
            [1, 2, 2, 3, 1, 4, 2],
        ]
        ___ nums __ testCases:
            print('nums: %s' % nums)
            result = findShortestSubArray(nums)
            print('result: %s' % result)
            print('-='*30+'-')

__ __name__ __ '__main__':
    Solution().test()
