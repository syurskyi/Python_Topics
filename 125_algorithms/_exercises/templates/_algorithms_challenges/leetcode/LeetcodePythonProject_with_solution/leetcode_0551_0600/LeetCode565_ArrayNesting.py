'''
Created on Aug 30, 2017

@author: MT
'''
class Solution(object):
    ___ arrayNesting(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        hashmap = {}
        maxLen = 0
        ___ num __ nums:
            __ num n.. __ hashmap:
                hashset = set()
                count = 0
                num0 = num
                w.... num0 != num o. count __ 0:
                    count += 1
                    num0 = nums[num0]
                    hashset.add(num0)
                ___ num0 __ hashset:
                    hashmap[num0] = count
                maxLen = max(maxLen, count)
        r.. maxLen
    
    ___ test(self):
        testCases = [
            [5,4,0,3,1,6,2],
            [0],
        ]
        ___ nums __ testCases:
            print('nums: %s' % nums)
            result = self.arrayNesting(nums)
            print('result: %s' % result)
            print('-='*30+'-')

__ __name__ __ '__main__':
    Solution().test()
