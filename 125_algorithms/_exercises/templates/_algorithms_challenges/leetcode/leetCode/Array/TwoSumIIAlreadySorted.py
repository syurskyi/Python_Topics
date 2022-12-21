"""
Given an array of integers that is already sorted in ascending order, find two numbers such that they add up to a specific target number.

The function twoSum should return indices of the two numbers such that they add up to the target, where index1 must be less than index2.

Note:

Your returned answers (both index1 and index2) are not zero-based.
You may assume that each input would have exactly one solution and you may not use the same element twice.
Example:

Input: numbers = [2,7,11,15], target = 9
Output: [1,2]
Explanation: The sum of 2 and 7 is 9. Therefore index1 = 1, index2 = 2.

Two Sum 已经排序后的输出，直接可以O(n):

解释传送门：
TwoSum.
ThreeSum.

"""
c.. Solution o..
    ___ twoSum  sortedNums, target
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        start = 0
        end = l..(sortedNums) - 1
        _____ start <= end:
            # print(nums[start] + nums[end])
            __ sortedNums[start] + sortedNums[end] __ target:
                r_ start+1, end+1
            
            __ sortedNums[start] + sortedNums[end] > target:
                end -= 1
            ____
                start += 1

