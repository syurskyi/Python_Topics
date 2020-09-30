# Trapping Rain Water
# Question: Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it is able to trap after raining.
# For example,
# Given [0,1,0,2,1,0,1,3,2,1,2,1], return 6.
# Solutions:


class Solution:
    # @param {integer[]} height
    # @return {integer}
    ___ trap(self, height):
        if not height or len(height)==1:
            r_ 0
        max_left = height[0]
        AddVolume = [max_left]

        ___ i __ ra..(1,len(height)-1):
            if max_left < height[i-1]:
                max_left = height[i-1]
            AddVolume.append(max_left)

        max_right = height[-1]
        AddVolume.append(max_right)

        ___ i __ reversed(ra..(1,len(height)-1)):
            if max_right < height[i+1]:
                    max_right = height[i+1]
            AddVolume[i] = min(max_right,AddVolume[i])
        ___ i __ ra..(len(AddVolume)):
            AddVolume[i] = ma.(AddVolume[i] - height[i],0)
        r_ sum(AddVolume)


Solution().trap([0,1,0,2,1,0,1,3,2,1,2,1])