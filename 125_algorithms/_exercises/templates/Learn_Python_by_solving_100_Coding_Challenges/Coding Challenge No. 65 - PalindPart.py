# Palindrome Partitioning
# Question: Given a string s, partition s such that every substring of the partition is a palindrome. Return all possible palindrome partitioning of s.
# For example: given s = "aab"
# Return [ ["aa","b"], ["a","a","b"] ].
# Solutions:


class Solution:
    # @param s, a string
    # @return a boolean
    ___ _isPalindrome(self, s):
        begin, end = 0, len(s)-1
        while begin < end:
            if s[begin] != s[end]:
                r_ False
            else:
                begin += 1
                end -= 1
        r_ True

    # @param s, a string
    # @return a list of lists of string

    ___ partition(self, s):
        if len(s) == 0:
            r_   # list
        if len(s) == 1:
            r_ [[s]]
        result =   # list
        if self._isPalindrome(s):
            result.append([s])

        ___ i __ ra..(1, len(s)):
            head = s[:i]
            if not self._isPalindrome(head):
                continue
            tailPartition = self.partition(s[i:])
            result.extend([[head] + item ___ item __ tailPartition])
        r_ result


Solution().partition("aab")