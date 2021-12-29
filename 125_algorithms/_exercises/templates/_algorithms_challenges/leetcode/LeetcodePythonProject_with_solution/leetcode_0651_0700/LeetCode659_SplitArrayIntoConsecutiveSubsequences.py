'''
Created on Oct 7, 2017

@author: MT
'''
class Solution(object):
    ___ isPossible(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        freqMap, appendFreqMap = {}, {}
        ___ num __ nums:
            freqMap[num] = freqMap.get(num, 0)+1
        ___ num __ nums:
            __ freqMap[num] __ 0:
                continue
            ____ appendFreqMap.get(num, 0) > 0:
                appendFreqMap[num] -= 1
                appendFreqMap[num+1] = appendFreqMap.get(num+1, 0)+1
            ____ freqMap.get(num+1, 0)>0 and freqMap.get(num+2, 0)>0:
                freqMap[num+1] -= 1
                freqMap[num+2] -= 1
                appendFreqMap[num+3] = appendFreqMap.get(num+3, 0)+1
            ____:
                r.. False
            freqMap[num] -= 1
        r.. True
    
    ___ test(self):
        testCases = [
            [1, 2, 3, 3, 4, 5],
            [1, 2, 2, 3, 3, 3, 4, 4, 5],
            [1, 2, 3, 3, 4, 4, 5, 5],
            [1, 2, 3, 4, 4, 5],
        ]
        ___ nums __ testCases:
            print('nums: %s' % nums)
            result = self.isPossible(nums)
            print('result: %s' % result)
            print('-='*30+'-')

__ __name__ __ '__main__':
    Solution().test()
