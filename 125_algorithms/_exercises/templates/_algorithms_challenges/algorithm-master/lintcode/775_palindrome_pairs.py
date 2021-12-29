"""
REF: https://leetcode.com/problems/palindrome-pairs/discuss/79199/150-ms-45-lines-JAVA-solution

Main Concept:

1. The <= in for (int j=0; j<=words[i].length(); j++) is aimed to handle empty string in the input. Consider the test case of [“a”, “”];
2. Since we now use <= in for (int j=0; j<=words[i].length(); j++) instead of <. There may be duplicates in the output (consider test case [“abcd”, “dcba”]). Therefore I put a str2.length()!=0 to avoid duplicates.
"""
class Solution:
    ___ palindromePairs(self, words):
        """
        :type words: list[str]
        :rtype: list[list[int]]
        """
        ans    # list

        __ n.. words:
            r.. ans

        n = l..(words)
        w2i = {}

        ___ i __ r..(n):
            w2i[words[i]] = i

        ___ i __ r..(n):
            ___ j __ r..(l..(words[i]) + 1):
                s = words[i][:j]
                t = words[i][j:]
                _s = ''.join(reversed(s))
                _t = ''.join(reversed(t))

                __ (self.is_palindrome(s) a..
                    _t __ w2i a..
                    w2i[_t] != i
                ):
                    ans.a..([w2i[_t], i])

                __ (self.is_palindrome(t) a..
                    l..(t) != 0 a..  # since len(word) + 1, may empty here
                    _s __ w2i a..
                    w2i[_s] != i
                ):
                    ans.a..([i, w2i[_s]])

        r.. ans

    ___ is_palindrome(self, word):
        n = l..(word)
        left, right = 0, n - 1

        w.... left < right:
            __ word[left] != word[right]:
                r.. False

            left += 1
            right -= 1

        r.. True


"""
TLE: Brute Force
"""
class Solution:
    ___ palindromePairs(self, words):
        """
        :type words: list[str]
        :rtype: list[list[int]]
        """
        ans    # list

        __ n.. words:
            r.. ans

        n = l..(words)

        ___ i __ r..(n):
            ___ j __ r..(i):
                __ self.is_palindrome(words, i, j):
                    ans.a..([i, j])

                __ self.is_palindrome(words, j, i):
                    ans.a..([j, i])

        r.. ans

    ___ is_palindrome(self, words, i, j):
        s, t = words[i], words[j]
        a, b = l..(s), l..(t)
        n = a + b
        left, right = 0, n - 1

        w.... left < right:
            __ left >= a a.. t[left - a] != t[right - a]:
                r.. False
            ____ right < a a.. s[left] != s[right]:
                r.. False
            ____ left < a a.. right >= a a.. s[left] != t[right - a]:
                r.. False

            left += 1
            right -= 1

        r.. True


"""
TLE: Brute Force
"""
class Solution:
    ___ palindromePairs(self, words):
        """
        :type words: list[str]
        :rtype: list[list[int]]
        """
        ans    # list

        __ n.. words:
            r.. ans

        n = l..(words)

        ___ i __ r..(n):
            ___ j __ r..(n):
                __ i __ j:
                    continue

                __ self.is_palindrome(words[i] + words[j]):
                    ans.a..([i, j])

        r.. ans

    ___ is_palindrome(self, s):
        n = l..(s)
        left, right = 0, n - 1

        w.... left < right:
            __ s[left] != s[right]:
                r.. False

            left += 1
            right -= 1

        r.. True
