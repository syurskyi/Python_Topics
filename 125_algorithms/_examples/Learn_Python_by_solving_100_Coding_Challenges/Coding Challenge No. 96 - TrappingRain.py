# Trapping Rain Water
# Question: Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it is able to trap after raining.
# For example,
# Given [0,1,0,2,1,0,1,3,2,1,2,1], return 6.
# Solutions:


class Solution:
    # @param {integer[]} height
    # @return {integer}
    def trap(self, height):
        if not height or len(height)==1:
            return 0
        max_left = height[0]
        AddVolume = [max_left]

        for i in range(1,len(height)-1):
            if max_left < height[i-1]:
                max_left = height[i-1]
            AddVolume.append(max_left)

        max_right = height[-1]
        AddVolume.append(max_right)

        for i in reversed(range(1,len(height)-1)):
            if max_right < height[i+1]:
                    max_right = height[i+1]
            AddVolume[i] = min(max_right,AddVolume[i])
        for i in range(len(AddVolume)):
            AddVolume[i] = max(AddVolume[i] - height[i],0)
        return sum(AddVolume)


Solution().trap([0,1,0,2,1,0,1,3,2,1,2,1])