c_ Solution:
    ___ longestPalindrome s: st.)  st.:
        n _ le.(s)
        __(n<2
            r_ s
        left _ 0
        right _ 0

        palindrome _ [[0]*n ___ _ __ ra..(n)]

        ___ j __ ra..(1,n
            ___ i __ ra..(0,j
                innerIsPalindrome _ palindrome[i+1][j-1] o.. j-i<_2
                __(s[i] __ s[j] a.. innerIsPalindrome
                    palindrome[i][j] _ T..
                    __(j-i>right-left
                        left _ i
                        right _ j

        r_ s[left:right+1]