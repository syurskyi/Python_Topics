"""
Given a string, find the length of the longest substring without repeating characters. For example, the longest
substring without repeating letters for "abcabcbb" is "abc", which the length is 3. For "bbbbb" the longest substring
is "b", with the length of 1.
"""
__author__ = 'Danyang'


class Solution:
    ___ lengthOfLongestSubstring(self, s):
        """
        Algorithm: Hash Map, two pointers
        Hash Map: array visited = [] for all ascii, notice the algorithm of updating this array
        Two pointers: start - start of the string; ind - scanning

        Given a string, find the length of the longest substring without repeating characters.
        :param s: String
        :return: Integer
        """
        # last visited index in the string
        visited_last_index = [-1 ___ _ __ r..(256)]  # ascii
        longest = 0  # record result

        start = 0  # pointer
        ___ ind, val __ enumerate(s):
            __ visited_last_index[ord(val)] __ -1:
                longest = max(longest, (ind)-start+1)
            ____:
                longest = max(longest, (ind-1)-start+1)

                # unmark
                ___ i __ r..(start, visited_last_index[ord(val)]):
                    visited_last_index[ord(s[i])] = -1

                start = visited_last_index[ord(val)]+1

            visited_last_index[ord(val)] = ind  # update last visited index

        r.. longest