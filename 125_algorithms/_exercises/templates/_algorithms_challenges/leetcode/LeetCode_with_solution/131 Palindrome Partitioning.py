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
__author__ 'Danyang'
c_ Solution:
    ___ partition  s
        """
        dfs
        :param s: string
        :return: a list of lists of string
        """
        result    # list
        get_partition(s, [], result)
        r.. result

    ___ get_partition  seq, cur, result
        __ n.. seq:
            result.a..(cur)

        # partition seq
        ___ i __ x..(l..(seq:
            __ is_palindrome(seq[:i+1]  # otherwise prune
                get_partition(seq[i+1:], cur+[seq[:i+1]], result)


    ___ is_palindrome  s
        # O(n)
        # return s == reversed(s)  # error, need to use ''.join(reversed(s))
        r.. s __ s[::-1]

__ _____ __ ____
    ... Solution().partition("aab")__[['a', 'a', 'b' ,  'aa', 'b']]
