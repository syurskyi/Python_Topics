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

    def longestConsecutive(self, num):
        startToEnd = {}
        endToStart = {}
        longest = 0
        for i in range(0, len(num)):
            start = num[i]
            end = num[i]
            if num[i] in startToEnd:
                end = startToEnd[num[i]]
                del startToEnd[num[i]]
                del endToStart[end]
            if num[i] in endToStart:
                start = endToStart[num[i]]
                del startToEnd[start]
                del endToStart[num[i]]
            if num[i]-1 in endToStart:
                start = min(start, endToStart[num[i]-1])
                del startToEnd[endToStart[num[i]-1]]
                del endToStart[num[i]-1]
            if num[i]+1 in startToEnd:
                end = max(end, startToEnd[num[i]+1])
                del endToStart[startToEnd[num[i]+1]]
                del startToEnd[num[i]+1]
            startToEnd[start] = end
            endToStart[end] = start
            longest = max(longest, end-start+1)
        return longest

Solution().longestConsecutive( [100, 4, 200, 1, 3, 2] )