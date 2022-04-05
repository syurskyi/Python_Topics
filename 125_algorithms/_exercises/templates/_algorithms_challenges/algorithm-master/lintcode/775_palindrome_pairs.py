"""
REF: https://leetcode.com/problems/palindrome-pairs/discuss/79199/150-ms-45-lines-JAVA-solution

Main Concept:

1. The <= in for (int j=0; j<=words[i].length(); j++) is aimed to handle empty string in the input. Consider the test case of [“a”, “”];
2. Since we now use <= in for (int j=0; j<=words[i].length(); j++) instead of <. There may be duplicates in the output (consider test case [“abcd”, “dcba”]). Therefore I put a str2.length()!=0 to avoid duplicates.
"""
c_ Solution:
    ___ palindromePairs  words
        """
        :type words: list[str]
        :rtype: list[list[int]]
        """
        ans    # list

        __ n.. words:
            r.. ans

        n = l..(words)
        w2i    # dict

        ___ i __ r..(n
            w2i[words[i]] = i

        ___ i __ r..(n
            ___ j __ r..(l..(words[i]) + 1
                s = words[i][:j]
                t = words[i][j:]
                _s = ''.j..(r..(s
                _t = ''.j..(r..(t

                __ (is_palindrome(s) a..
                    _t __ w2i a..
                    w2i[_t] != i

                    ans.a..([w2i[_t], i])

                __ (is_palindrome(t) a..
                    l..(t) != 0 a..  # since len(word) + 1, may empty here
                    _s __ w2i a..
                    w2i[_s] != i

                    ans.a..([i, w2i[_s]])

        r.. ans

    ___ is_palindrome  word
        n = l..(word)
        left, right = 0, n - 1

        w.... left < right:
            __ word[left] != word[right]:
                r.. F..

            left += 1
            right -_ 1

        r.. T..


"""
TLE: Brute Force
"""
c_ Solution:
    ___ palindromePairs  words
        """
        :type words: list[str]
        :rtype: list[list[int]]
        """
        ans    # list

        __ n.. words:
            r.. ans

        n = l..(words)

        ___ i __ r..(n
            ___ j __ r..(i
                __ is_palindrome(words, i, j
                    ans.a..([i, j])

                __ is_palindrome(words, j, i
                    ans.a..([j, i])

        r.. ans

    ___ is_palindrome  words, i, j
        s, t = words[i], words[j]
        a, b = l..(s), l..(t)
        n = a + b
        left, right = 0, n - 1

        w.... left < right:
            __ left >_ a a.. t[left - a] != t[right - a]:
                r.. F..
            ____ right < a a.. s[left] != s[right]:
                r.. F..
            ____ left < a a.. right >_ a a.. s[left] != t[right - a]:
                r.. F..

            left += 1
            right -_ 1

        r.. T..


"""
TLE: Brute Force
"""
c_ Solution:
    ___ palindromePairs  words
        """
        :type words: list[str]
        :rtype: list[list[int]]
        """
        ans    # list

        __ n.. words:
            r.. ans

        n = l..(words)

        ___ i __ r..(n
            ___ j __ r..(n
                __ i __ j:
                    _____

                __ is_palindrome(words[i] + words[j]
                    ans.a..([i, j])

        r.. ans

    ___ is_palindrome  s
        n = l..(s)
        left, right = 0, n - 1

        w.... left < right:
            __ s[left] != s[right]:
                r.. F..

            left += 1
            right -_ 1

        r.. T..
