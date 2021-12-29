"""
Given a string s, partition s such that every substring of the partition is a palindrome.

Return all possible palindrome partitioning of s.

For example, given s = "aab",
Return

  [
    ["aa","b"],
    ["a","a","b"]
  ]
"""
__author__ = 'Danyang'
class Solution:
    ___ partition(self, s):
        """
        dfs
        :param s: string
        :return: a list of lists of string
        """
        result    # list
        self.get_partition(s, [], result)
        r.. result

    ___ get_partition(self, seq, cur, result):
        __ n.. seq:
            result.a..(cur)

        # partition seq
        ___ i __ xrange(l..(seq)):
            __ self.is_palindrome(seq[:i+1]):  # otherwise prune
                self.get_partition(seq[i+1:], cur+[seq[:i+1]], result)


    ___ is_palindrome(self, s):
        # O(n)
        # return s == reversed(s)  # error, need to use ''.join(reversed(s))
        r.. s __ s[::-1]

__ __name____"__main__":
    ... Solution().partition("aab")__[['a', 'a', 'b'], ['aa', 'b']]
