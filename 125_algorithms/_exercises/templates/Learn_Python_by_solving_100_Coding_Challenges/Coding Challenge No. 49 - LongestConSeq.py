# Longest Consecutive Sequence
# Question: Given an unsorted array of integers, find the length of the longest consecutive elements sequence.
# For example,
# Given [100, 4, 200, 1, 3, 2],
# The longest consecutive elements sequence is [1, 2, 3, 4]. Return its length: 4.
# Your algorithm should run in O(n) complexity.
# Solutions:


class Solution:
    # @param num, a list of integer
    # @return an integer

    ___ longestConsecutive(self, num):
        startToEnd _ {}
        endToStart _ {}
        longest _ 0
        ___ i __ ra..(0, le.(num)):
            start _ num[i]
            end _ num[i]
            __ num[i] __ startToEnd:
                end _ startToEnd[num[i]]
                del startToEnd[num[i]]
                del endToStart[end]
            __ num[i] __ endToStart:
                start _ endToStart[num[i]]
                del startToEnd[start]
                del endToStart[num[i]]
            __ num[i]-1 __ endToStart:
                start _ mi.(start, endToStart[num[i]-1])
                del startToEnd[endToStart[num[i]-1]]
                del endToStart[num[i]-1]
            __ num[i]+1 __ startToEnd:
                end _ ma.(end, startToEnd[num[i]+1])
                del endToStart[startToEnd[num[i]+1]]
                del startToEnd[num[i]+1]
            startToEnd[start] _ end
            endToStart[end] _ start
            longest _ ma.(longest, end-start+1)
        r_ longest

Solution().longestConsecutive( [100, 4, 200, 1, 3, 2] )