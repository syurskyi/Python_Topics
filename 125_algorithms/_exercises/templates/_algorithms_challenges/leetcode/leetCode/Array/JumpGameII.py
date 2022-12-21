"""
Given an array of non-negative integers, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Your goal is to reach the last index in the minimum number of jumps.

Example:

Input: [2,3,1,1,4]
Output: 2
Explanation: The minimum number of jumps to reach the last index is 2.
    Jump 1 step from index 0 to 1, then 3 steps to the last index.
Note:

You can assume that you can always reach the last index.

与 1 差不多，这个需要返回的是最少的可用步数。

因为 1 中直接返回的是最大的，所以可以顺便把 2 也给完成。

beat 66%.

测试地址：
https://leetcode.com/problems/jump-game-ii/description/

"""
c.. Solution o..
    ___ jump  nums
        """
        :type nums: List[int]
        :rtype: int
        """
        __ l..(nums) __ 1:
            r_ 0
        
        # dp = [nums[0]]
        maxes = nums[0]
        count = 1
        current_index = 0
        length = l..(nums) - 1
        _____ 1:
            __ current_index + maxes >= length:
                r_ count
            base = 0
            index = current_index
            ___ i __ xrange(current_index, current_index+maxes+1
                __ nums[i] + i > base:
                    base = nums[i] + i
                    index = i
                      
            current_index = index
            maxes = base-index
            count += 1