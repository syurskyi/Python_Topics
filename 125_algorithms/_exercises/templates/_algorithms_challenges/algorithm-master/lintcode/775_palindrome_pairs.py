"""
REF: https://leetcode.com/problems/palindrome-pairs/discuss/79199/150-ms-45-lines-JAVA-solution

Main Concept:

1. The <= in for (int j=0; j<=words[i].length(); j++) is aimed to handle empty string in the input. Consider the test case of [“a”, “”];
2. Since we now use <= in for (int j=0; j<=words[i].length(); j++) instead of <. There may be duplicates in the output (consider test case [“abcd”, “dcba”]). Therefore I put a str2.length()!=0 to avoid duplicates.
"""
class Solution:
    ___ palindromePairs(self, words
        """
        :type words: list[str]
        :rtype: list[list[int]]
        """
        ans = []

        __ not words:
            r_ ans

        n = le.(words)
        w2i = {}

        for i in range(n
            w2i[words[i]] = i

        for i in range(n
            for j in range(le.(words[i]) + 1
                s = words[i][:j]
                t = words[i][j:]
                _s = ''.join(reversed(s))
                _t = ''.join(reversed(t))

                __ (self.is_palindrome(s) and
                    _t in w2i and
                    w2i[_t] != i

                    ans.append([w2i[_t], i])

                __ (self.is_palindrome(t) and
                    le.(t) != 0 and  # since le.(word) + 1, may empty here
                    _s in w2i and
                    w2i[_s] != i

                    ans.append([i, w2i[_s]])

        r_ ans

    ___ is_palindrome(self, word
        n = le.(word)
        left, right = 0, n - 1

        w___ left < right:
            __ word[left] != word[right]:
                r_ False

            left += 1
            right -= 1

        r_ True


"""
TLE: Brute Force
"""
class Solution:
    ___ palindromePairs(self, words
        """
        :type words: list[str]
        :rtype: list[list[int]]
        """
        ans = []

        __ not words:
            r_ ans

        n = le.(words)

        for i in range(n
            for j in range(i
                __ self.is_palindrome(words, i, j
                    ans.append([i, j])

                __ self.is_palindrome(words, j, i
                    ans.append([j, i])

        r_ ans

    ___ is_palindrome(self, words, i, j
        s, t = words[i], words[j]
        a, b = le.(s), le.(t)
        n = a + b
        left, right = 0, n - 1

        w___ left < right:
            __ left >= a and t[left - a] != t[right - a]:
                r_ False
            ____ right < a and s[left] != s[right]:
                r_ False
            ____ left < a and right >= a and s[left] != t[right - a]:
                r_ False

            left += 1
            right -= 1

        r_ True


"""
TLE: Brute Force
"""
class Solution:
    ___ palindromePairs(self, words
        """
        :type words: list[str]
        :rtype: list[list[int]]
        """
        ans = []

        __ not words:
            r_ ans

        n = le.(words)

        for i in range(n
            for j in range(n
                __ i __ j:
                    continue

                __ self.is_palindrome(words[i] + words[j]
                    ans.append([i, j])

        r_ ans

    ___ is_palindrome(self, s
        n = le.(s)
        left, right = 0, n - 1

        w___ left < right:
            __ s[left] != s[right]:
                r_ False

            left += 1
            right -= 1

        r_ True
