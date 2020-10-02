# Trapping Rain Water
# Question: Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it is able to trap after raining.
# For example,
# Given [0,1,0,2,1,0,1,3,2,1,2,1], return 6.
# Solutions:


c_ Solution:
    # @param {integer[]} height
    # @return {integer}
    ___ trap , height:
        __ no. height o. le. height__1:
            r_ 0
        max_left _ height[0]
        AddVolume _ [max_left]

        ___ i __ ra.. 1,le. height-1:
            __ max_left < height[i-1]:
                max_left _ height[i-1]
            AddVolume.ap.. max_left

        max_right _ height[-1]
        AddVolume.ap.. max_right

        ___ i __ r.. ra.. 1,le. height-1:
            __ max_right < height[i+1]:
                    max_right _ height[i+1]
            AddVolume[i] _ mi. max_right,AddVolume[i]
        ___ i __ ra.. le. AddVolume:
            AddVolume[i] _ ma. AddVolume[i] - height[i],0
        r_ su. AddVolume


Solution .trap [0,1,0,2,1,0,1,3,2,1,2,1]