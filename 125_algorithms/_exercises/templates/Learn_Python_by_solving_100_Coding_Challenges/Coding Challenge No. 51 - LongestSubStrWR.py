# Longest Substring without Repeating Characters
# Question: Given a string, find the length of the longest substring without repeating characters. For example:
# Given "abcabcbb", the answer is "abc", which the length is 3.
# Given "bbbbb", the answer is "b", with the length of 1.
# Given "pwwkew", the answer is "wke", with the length of 3.
# Solutions:


c_ Solution:
    # @return an integer
    ___ lengthOfLongestSubstring(, s):
        lastRepeating _ -1
        longestSubstring _ 0
        positions _ {}
        ___ i __ ra..(0, le.(s)):
            __ s[i] __ positions an. lastRepeating<positions[s[i]]:
                lastRepeating _ positions[s[i]]
            __ i-lastRepeating > longestSubstring:
                longestSubstring _ i-lastRepeating
            positions [s[i]]_i
        r_ longestSubstring


Solution().lengthOfLongestSubstring("abcabcbb")